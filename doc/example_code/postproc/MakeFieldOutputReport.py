from odbAccess import openOdb
from abapy.postproc import MakeFieldOutputReport
# Some settings
odb_name = 'indentation.odb'
report_name = 'indentation_core_step0_frame1_S11_nodes.rpt'
step = 0
frame = -1
new_position = 'NODAL'
original_position = 'INTEGRATION_POINT'
field = 'S'
sub_field = 11
instance = 'I_SAMPLE'
sub_set = 'CORE'
sub_set_type = 'element'
# Function testing
odb = openOdb(odb_name)
MakeFieldOutputReport(
  odb = odb, 
  instance = instance, 
  step = step,
  frame = frame,
  report_name = report_name, 
  original_position = original_position, 
  new_position = new_position, 
  field = field, 
  sub_field = sub_field, 
  sub_set_type = sub_set_type, 
  sub_set = sub_set)
new_position = 'INTEGRATION_POINT'
report_name = 'indentation_core_step0_frame1_S11_elements.rpt'   
MakeFieldOutputReport(
  odb = odb, 
  instance = instance, 
  step = step,
  frame = frame,
  report_name = report_name, 
  original_position = original_position, 
  new_position = new_position, 
  field = field, 
  sub_field = sub_field, 
  sub_set_type = sub_set_type, 
  sub_set = sub_set)
new_position = 'ELEMENT_NODAL'
report_name = 'indentation_core_step0_frame1_S11_element-nodal.rpt'   
MakeFieldOutputReport(
  odb = odb, 
  instance = instance, 
  step = step,
  frame = frame,
  report_name = report_name, 
  original_position = original_position, 
  new_position = new_position, 
  field = field, 
  sub_field = sub_field, 
  sub_set_type = sub_set_type, 
  sub_set = sub_set)
field = 'U'
sub_field = 'Magnitude'
original_position = 'NODAL'
new_position = 'NODAL'
report_name = 'indentation_core_step0_frame1_U-MAG_nodal.rpt'   
MakeFieldOutputReport(
  odb = odb, 
  instance = instance, 
  step = step,
  frame = frame,
  report_name = report_name, 
  original_position = original_position, 
  new_position = new_position, 
  field = field, 
  sub_field = sub_field, 
  sub_set_type = sub_set_type, 
  sub_set = sub_set)