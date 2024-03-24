# RegEX for drawing the hanged man
top = '\t'+('-'*16)
bod_head = '\t||'+(' '*12)+'O'
bod_headx = '\t||'+(' '*12)+'0'
neck = '\n\t||'+(' '*11)+'-+-'
left_arm = '\n\t||'+(' '*10)+'/'
right_arm = '\n\t||'+(' '*10)+'/'+(' '*3)+'\\'
body = '\n\t||'+(' '*10)+'/'+(' '*1)+'|'+(' '*1)+'\\' + '\n\t||'+' '*12+'|'
left_leg = '\n\t||'+(' '*11)+'/' + '\n\t||'+(' '*10)+'/'
right_leg = '\n\t||'+(' '*11)+'/'+(' '*1)+'\\' + '\n\t||'+(' '*10)+'/'+(' '*3)+'\\'
gallow = ('\n\t||')
gallow_head = ('\n\t||'*5)
gallow_neck = ('\n\t||'*4)
gallow_body = ('\n\t||'*3)
gallow_bodyx = ('\n\t||'*2)
bottom = '\t'+('-'*23)