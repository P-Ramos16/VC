import numpy as np
import cv2
import glob

# Função para remover a distorção da imagem
def undistort_image(img, intrinsics, distortion):
    h, w = img.shape[:2]
    new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(intrinsics, distortion, (w, h), 1, (w, h))
    undistorted_img = cv2.undistort(img, intrinsics, distortion, None, new_camera_matrix)
    return undistorted_img

# Carregar os parâmetros de calibração
calibration_params = np.load("stereoParams.npz")
intrinsics1 = calibration_params['intrinsics1']
distortion1 = calibration_params['distortion1']
intrinsics2 = calibration_params['intrinsics2']
distortion2 = calibration_params['distortion2']
F = calibration_params['F']

# Selecionar um par estéreo de imagens
left_images = sorted(glob.glob('..//images//left*.jpg'))
right_images = sorted(glob.glob('..//images//right*.jpg'))

if left_images and right_images:
    # Carregar um par estéreo
    left_img = cv2.imread(left_images[0])
    right_img = cv2.imread(right_images[0])

    # Remover a distorção das imagens
    undistorted_left = undistort_image(left_img, intrinsics1, distortion1)
    undistorted_right = undistort_image(right_img, intrinsics2, distortion2)

    # Converter as imagens para escala de cinza
    gray_left = cv2.cvtColor(undistorted_left, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(undistorted_right, cv2.COLOR_BGR2GRAY)

    # Mostrar as imagens retificadas em escala de cinza
    cv2.imshow('Left Image - Undistorted', gray_left)
    cv2.imshow('Right Image - Undistorted', gray_right)

    # Obter as dimensões da imagem
    h, w = gray_left.shape[:2]

    # Inicializar as matrizes de rotação e projeção
    R = np.eye(3, dtype=np.float64)
    T = np.array([1, 0, 0], dtype=np.float64)
    R1 = np.zeros((3, 3), dtype=np.float64)
    R2 = np.zeros((3, 3), dtype=np.float64)
    P1 = np.zeros((3, 4), dtype=np.float64)
    P2 = np.zeros((3, 4), dtype=np.float64)
    Q = np.zeros((4, 4), dtype=np.float64)

    # Calcular as matrizes de retificação usando cv2.stereoRectify
    cv2.stereoRectify(intrinsics1, distortion1, intrinsics2, distortion2, (w, h), R, T, R1, R2, P1, P2, Q, flags=cv2.CALIB_ZERO_DISPARITY, alpha=-1, newImageSize=(0, 0))

    # Mapas de retificação
    map1x, map1y = cv2.initUndistortRectifyMap(intrinsics1, distortion1, R1, P1, (w, h), cv2.CV_32FC1)
    map2x, map2y = cv2.initUndistortRectifyMap(intrinsics2, distortion2, R2, P2, (w, h), cv2.CV_32FC1)

    # Aplicar a retificação usando cv2.remap
    rectified_left = cv2.remap(gray_left, map1x, map1y, cv2.INTER_LINEAR)
    rectified_right = cv2.remap(gray_right, map2x, map2y, cv2.INTER_LINEAR)

    # Inicializar o objeto StereoBM para correspondência de blocos
    stereo = cv2.StereoBM_create(numDisparities=16*5, blockSize=21)

    # Calcular o mapa de disparidade
    disparity = stereo.compute(rectified_left, rectified_right)

    # Normalizar o mapa de disparidade
    disparity = cv2.normalize(src=disparity, dst=disparity, beta=0, alpha=255, norm_type=cv2.NORM_MINMAX)
    disparity = np.uint8(disparity)

    # Calcular as coordenadas 3D usando cv2.reprojectImageTo3D
    points_3d = cv2.reprojectImageTo3D(disparity, Q)

    # Salvar as coordenadas 3D em um arquivo .npz
    np.savez('3d_coordinates.npz', points=points_3d)

    # Mostrar as imagens retificadas e mapa de disparidade
    cv2.imshow('Left Image - Rectified', rectified_left)
    cv2.imshow('Right Image - Rectified', rectified_right)
    cv2.imshow('Disparity Map', disparity)

    # Aguarda interação e fecha janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Não foram encontradas imagens estéreo para processamento.")