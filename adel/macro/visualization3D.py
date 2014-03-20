def visualization3D(stand_MTG):
    # colors
    colors = [[0, 255, 0], [255, 0, 0], [0, 255, 0], [255, 0, 0], [0, 255, 0], [255, 0, 0], [0, 255, 0], [255, 0, 0], [0, 255, 0], [255, 0, 0], [0, 255, 0], [255, 0, 0]]
    # col_item
    from alinea.adel.povray import povray
    lambda_function = povray.col_item(None, colors)
    # apply_property
    from alinea.adel import mtg
    new_values = mtg.apply_property(stand_MTG, 'tissue_type', lambda_function)
    # to_plantgl
    plantgl_scene = mtg.to_plantgl(stand_MTG, (0,180,0), (0, 130, 0), (170,85,0), new_values, True)[0]
    # plot3D
    from openalea.plantgl.wralea.visualization import viewernode
    viewernode.Plot3D(plantgl_scene)
    return plantgl_scene, 