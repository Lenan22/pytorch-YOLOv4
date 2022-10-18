import onnx

onnx_model = onnx.load("yolov4_1_3_608_608_static_sim.onnx")
graph = onnx_model.graph
node  = graph.node

nodes_need_to_del = []
node_output_flags = {"output", "output.3", "output.7"}

def matching_flags(node_single , node_output_flags):
    for name in node_single.input:
        if name in node_output_flags:
            return True
    return False    


for i in range(len(node)):
    assert (len(node[i].output)==1)
    if matching_flags(node[i], node_output_flags):
        nodes_need_to_del.append(node[i]) 
        node_output_flags.add(node[i].output[0])


for tmp_node in nodes_need_to_del:
    # assert (len(node[i].output)==1)
    graph.node.remove(tmp_node)  


onnx.save(onnx_model, 'yolov4-tiny.onnx')

    # if i > 184:
    #     nodes_need_to_del.append(node[i])
    # print(i)
    # print(node[i].name)

# (Pdb) p node[i].input
# ['onnx::Conv_207', 'models.29.conv18.weight', 'models.29.conv18.bias']
# (Pdb) p node[i].output
# ['output']




# for old_node in nodes_need_to_del:
#    graph.node.remove(old_node)


# old_scale_node = node[157]
# new_scale_node = onnx.helper.make_node(
#     "Constant",
#     inputs=[],
#     outputs=['449'],
#     value=onnx.helper.make_tensor('value', onnx.TensorProto.FLOAT, [4], [1, 1, 1.81, 1.81])
# )
# graph.node.remove(old_scale_node)  
# graph.node.insert(157, new_scale_node) 

# # onnx.checker.check_model(onnx_model)
# graph.cleanup()
# onnx.save(onnx_model, 'out.onnx')
