
# coding: utf-8

# # QT Buttons 1
# 
# Generates a bunch of buttons puts them into a layout

# In[13]:


buttons =[]
i = 0
j = 4
no_of_butttons = 12
prefix='S'

for k in range (1,no_of_butttons+1):
    buttons.append('{}{}'.format(prefix,k))

print('\n*****************************\nButtons\n*****************************\n')


for b in buttons:
    string = 'QPushButton *b{} = new QPushButton(tr("{}"));\nconnect(b{},SIGNAL(clicked()),this,SLOT(b{}Clicked()));'.format(b,b,b,b)
    print(string)


for b in buttons:
    string = 'mainLayout->addWidget(b{}, {} , {});'.format(b,int(i/j),i%j)
    i += 1
    print(string)
    
print('\n*****************************\nSlot stubs\n*****************************\n')

for b in buttons:
    string ='void VentilsGui::b'+b+'Clicked(){\n\tqDebug()<<\"'+ b+' pressed.\";\n}'
    print(string)

print('\n*****************************\nSlot definitions\n*****************************\n')

for b in buttons:
    string ='void b'+b+'Clicked();'
    print(string)

