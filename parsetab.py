
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftHEX_AleftHEX_BleftDECleftBIN_AleftBIN_BleftREGleftLPARleftRPARleftCMDleftCOMMAleftNEWLINEBIN_A BIN_B CMD COMMA DEC HEX_A HEX_B LPAR NEWLINE REG RPAR start : code\n              |\n     code : code stmt\n             | stmt\n     stmt : CMD args NEWLINE\n             | CMD args\n     args : args COMMA arg\n             | arg\n     arg : literal LPAR literal RPAR\n            | literal\n     literal : HEX_A\n                | HEX_B\n                | DEC\n                | BIN_A\n                | BIN_B\n                | REG\n    '
    
_lr_action_items = {'$end':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,18,20,],[-2,0,-1,-4,-3,-6,-8,-10,-11,-12,-13,-14,-15,-16,-5,-7,-9,]),'CMD':([0,2,3,5,6,7,8,9,10,11,12,13,14,15,18,20,],[4,4,-4,-3,-6,-8,-10,-11,-12,-13,-14,-15,-16,-5,-7,-9,]),'HEX_A':([4,16,17,],[9,9,9,]),'HEX_B':([4,16,17,],[10,10,10,]),'DEC':([4,16,17,],[11,11,11,]),'BIN_A':([4,16,17,],[12,12,12,]),'BIN_B':([4,16,17,],[13,13,13,]),'REG':([4,16,17,],[14,14,14,]),'NEWLINE':([6,7,8,9,10,11,12,13,14,18,20,],[15,-8,-10,-11,-12,-13,-14,-15,-16,-7,-9,]),'COMMA':([6,7,8,9,10,11,12,13,14,18,20,],[16,-8,-10,-11,-12,-13,-14,-15,-16,-7,-9,]),'LPAR':([8,9,10,11,12,13,14,],[17,-11,-12,-13,-14,-15,-16,]),'RPAR':([9,10,11,12,13,14,19,],[-11,-12,-13,-14,-15,-16,20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'code':([0,],[2,]),'stmt':([0,2,],[3,5,]),'args':([4,],[6,]),'arg':([4,16,],[7,18,]),'literal':([4,16,17,],[8,8,19,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> code','start',1,'p_start','parser.py',21),
  ('start -> <empty>','start',0,'p_start','parser.py',22),
  ('code -> code stmt','code',2,'p_code','parser.py',30),
  ('code -> stmt','code',1,'p_code','parser.py',31),
  ('stmt -> CMD args NEWLINE','stmt',3,'p_stmt','parser.py',39),
  ('stmt -> CMD args','stmt',2,'p_stmt','parser.py',40),
  ('args -> args COMMA arg','args',3,'p_args','parser.py',45),
  ('args -> arg','args',1,'p_args','parser.py',46),
  ('arg -> literal LPAR literal RPAR','arg',4,'p_arg','parser.py',54),
  ('arg -> literal','arg',1,'p_arg','parser.py',55),
  ('literal -> HEX_A','literal',1,'p_literal','parser.py',64),
  ('literal -> HEX_B','literal',1,'p_literal','parser.py',65),
  ('literal -> DEC','literal',1,'p_literal','parser.py',66),
  ('literal -> BIN_A','literal',1,'p_literal','parser.py',67),
  ('literal -> BIN_B','literal',1,'p_literal','parser.py',68),
  ('literal -> REG','literal',1,'p_literal','parser.py',69),
]