#!/usr/bin/env python3

import mission_execution_control as mxc
import rospy
from aerostack_msgs.msg import ListOfBeliefs
import math
import time

def mission():
  last_code = "INIT"
  print("Starting mission...")

  print("TAKE_OFF...")
  mxc.executeTask('TAKE_OFF')

  print("PAY_ATTENTION_TO_QR_CODES...")
  mxc.startTask('PAY_ATTENTION_TO_QR_CODES')

  while(True):
    s = 0
    s, num = mxc.queryBelief('object(?N,qr_code)')
    s, message = mxc.queryBelief('object(qr,?L)')

    if s:
      executed_action = False
      t0 = time.clock()
      while(not executed_action):
        if message['L'] == "CW90" and (last_code != message['L'] or (time.clock() - t0) > 5):
          executed_action = True
          print("Received 'ROTATE CLOCKWISE 90'")
          mxc.executeTask('ROTATE', relative_angle = 90)
          last_code = message['L']
          mxc.removeBelief('object(qr,'+message['L']+')')
          mxc.removeBelief('object('+str(num['N'])+','+message['L']+')')
          mxc.removeBelief('code('+str(num['N'])+','+message['L']+')')
         
        if message['L'] == "CCW90" and (last_code != message['L'] or (time.clock() - t0) > 5):
          executed_action = True
          print("Received 'ROTATE COUNTERCLOCKWISE 90'")
          mxc.executeTask('ROTATE', relative_angle = 90)
          last_code = message['L']
          mxc.removeBelief('object(qr,'+message['L']+')')
          mxc.removeBelief('object('+str(num['N'])+','+message['L']+')')
          mxc.removeBelief('code('+str(num['N'])+','+message['L']+')')

        if message['L'] == "DOWN" and (last_code != message['L'] or (time.clock() - t0) > 5):
          executed_action = True
          print("Received 'DOWN'")
          mxc.executeTask('MOVE_VERTICAL', distance = -1)
          last_code = message['L']
          mxc.removeBelief('object(qr,'+message['L']+')')
          mxc.removeBelief('object('+str(num['N'])+','+message['L']+')')
          mxc.removeBelief('code('+str(num['N'])+','+message['L']+')')

        if message['L'] == "UP" and (last_code != message['L'] or (time.clock() - t0) > 5):
          executed_action = True
          print("Received 'UP'")
          mxc.executeTask('MOVE_VERTICAL', distance = 1)
          last_code = message['L']
          mxc.removeBelief('object(qr,'+message['L']+')')
          mxc.removeBelief('object('+str(num['N'])+','+message['L']+')')
          mxc.removeBelief('code('+str(num['N'])+','+message['L']+')')

        if message['L'] == "LAND" and (last_code != message['L'] or (time.clock() - t0) > 5):
          executed_action = True
          print("Received 'LAND'")
          mxc.executeTask('LAND')
          last_code = message['L']
          mxc.removeBelief('object(qr,'+message['L']+')')
          mxc.removeBelief('object('+str(num['N'])+','+message['L']+')')
          mxc.removeBelief('code('+str(num['N'])+','+message['L']+')')

        if message['L'] == "MOVE_LEFT" and (last_code != message['L'] or (time.clock() - t0) > 5):
          executed_action = True
          print("Received 'MOVE_LEFT'")
          mxc.startTask('MOVE_AT_SPEED', direction = "LEFT", speed = 0.15)
          last_code = message['L']
          mxc.removeBelief('object(qr,'+message['L']+')')
          mxc.removeBelief('object('+str(num['N'])+','+message['L']+')')
          mxc.removeBelief('code('+str(num['N'])+','+message['L']+')')

        if message['L'] == "MOVE_RIGHT" and (last_code != message['L'] or (time.clock() - t0) > 5):
          executed_action = True
          print("Received 'MOVE_RIGHT'")
          mxc.startTask('MOVE_AT_SPEED', direction = "RIGHT", speed = 0.15)
          last_code = message['L']
          mxc.removeBelief('object(qr,'+message['L']+')')
          mxc.removeBelief('object('+str(num['N'])+','+message['L']+')')
          mxc.removeBelief('code('+str(num['N'])+','+message['L']+')')    