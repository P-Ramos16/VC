""" pcd_point_cloud = o3d.data.PCDPointCloud()
pcd = o3d.io.read_point_cloud(pcd_point_cloud.path)

plane_model, inliers = pcd.segment_plane(distance_threshold=0.01,
                                         ransac_n=3,
                                         num_iterations=1000)
[a, b, c, d] = plane_model
print(f"Plane equation: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f} = 0")

inlier_cloud = pcd.select_by_index(inliers)
inlier_cloud.paint_uniform_color([1.0, 0, 0])
outlier_cloud = pcd.select_by_index(inliers, invert=True)
o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud],
                                  zoom=0.8,
                                  front=[-0.4999, -0.1659, -0.8499],
                                  lookat=[2.1813, 2.0619, 2.0999],
                                  up=[0.1204, -0.9852, 0.1215]) """


#aula_09_ex_04.py
import open3d as o3d

pcd = o3d.io.read_point_cloud("../depth_images/office2.pcd")  

planes = []

print(f" Plane |   x   |   y   |   z   |   d   |")
print(f" ------+-------+-------+-------+-------+")

for planeID in range(3):
    plane_model, inliers = pcd.segment_plane(distance_threshold=0.01,
                                                         ransac_n=3,
                                                         num_iterations=500)
    [a, b, c, d] = plane_model
    print(f"     {planeID} | {a:5.2f} | {b:5.2f} | {c:5.2f} | {d:5.2f} |")
    
    inlier_cloud = pcd.select_by_index(inliers)
    if planeID == 0:
        inlier_cloud.paint_uniform_color([1.0, 0, 0])
    elif planeID == 1:
        inlier_cloud.paint_uniform_color([0, 1.0, 0])
    else:
        inlier_cloud.paint_uniform_color([0, 0, 1.0])

    pcd = pcd.select_by_index(inliers, invert=True)
    planes.append(inlier_cloud)



o3d.visualization.draw_geometries(planes + [pcd])
