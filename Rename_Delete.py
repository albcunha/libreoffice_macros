import os
from os.path import join, realpath
import zipfile
from shutil import copyfile
import uno
from com.sun.star.beans import PropertyValue
from com.sun.star.awt.PosSize import POSSIZE
dialog_label = 'Rename File'
title_label = 'File: '
ok_label = 'OK'
cancel_label = 'Cancel'
error_file_not_saved = 'Error. Save file first'
delete_label = 'Are you sure you want to delete this file?'

def Rename( ):
    def addAwtModel(oDM,srv,sName,dProps):
        oCM = oDM.createInstance("com.sun.star.awt.UnoControl"+ srv +"Model")
        while dProps:
            prp = dProps.popitem()
            uno.invoke(oCM,"setPropertyValue",(prp[0],prp[1]))
            #works with awt.UnoControlDialogElement only:
            oCM.Name = sName
        oDM.insertByName(sName,oCM)

    '''Salva o arquivo e renomeia'''
    def UserFields(model, nome, valor):
   ### altera o valor do campo nome. 

        master = model.TextFieldMasters.getByName(FIELDMASTER_TEMPLATE % nome)
        master.Content = valor

    # cria uma instancia que permite a insercao no texto

        objfield = model.createInstance("com.sun.star.text.textfield.User")
        objfield.attachTextFieldMaster(master)

        return objfield
        
    context = uno.getComponentContext()
    smgr = context.ServiceManager    
    desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop",context)
    document = desktop.getCurrentComponent()  
    url = document.URL
    try:
        syspath = uno.fileUrlToSystemPath(url)
    except:
        #faz dialogo
        oDM = smgr.createInstance("com.sun.star.awt.UnoControlDialogModel")
        oDM.Title = dialog_label
        addAwtModel(oDM, 'FixedText','lblName',{
            'Label' : error_file_not_saved,
            'Align' : 1,
            }
                    )
                
        addAwtModel(oDM,'Button','btnOK',{
            'Label' : ok_label,
            'DefaultButton' : True,
            'PushButtonType' : 1,
            }
                    )
        
        oDialog = smgr.createInstance("com.sun.star.awt.UnoControlDialog")
        oDialog.setModel(oDM)
        
        h = 25
        y = 20
        for c in oDialog.getControls():
            c.setPosSize(10, y, 400, h, POSSIZE)
            y += h 
        oDialog.setPosSize(400,300,350,y+h,POSSIZE)
        oDialog.setVisible(True)
        x = oDialog.execute()
        if x:
            pass
        else:
            return False
        oDialog.dispose()
        oDM.dispose()
        return None
        
        
        
    texto_arquivo = str(syspath)
    arquivo = texto_arquivo[texto_arquivo.rfind('\\')+1:]
    caminho = texto_arquivo[:texto_arquivo.rfind('\\')+1]
    #faz dialogo
    oDM = smgr.createInstance("com.sun.star.awt.UnoControlDialogModel")
    oDM.Title = dialog_label
    addAwtModel(oDM,'FixedText','lblName',{
        'Label' : title_label, 
        }
                )
    addAwtModel(oDM,'Edit','txtName',{
        'Text':arquivo})
      
             
    addAwtModel(oDM,'Button','btnOK',{
        'Label' : ok_label,
        'DefaultButton' : True,
        'PushButtonType' : 1,
        }
                )
    addAwtModel(oDM,'Button','btnCancel',{
        'Label' : cancel_label,
        'PushButtonType' : 2,
        }
                )

    oDialog = smgr.createInstance("com.sun.star.awt.UnoControlDialog")
    oDialog.setModel(oDM)
    txtN = oDialog.getControl('txtName')
    
    h = 25
    y = 20
    for c in oDialog.getControls():
        c.setPosSize(10, y, 400, h, POSSIZE)
        y += h 
    oDialog.setPosSize(300,300,450,y+h,POSSIZE)
    oDialog.setVisible(True)
    x = oDialog.execute()
    if x:
        pass
    else:
        return False
        
    arquivo_novo = caminho + txtN.getText()
    oDialog.dispose()
    oDM.dispose()
    
    def urlify(path):
        return uno.systemPathToFileUrl(os.path.realpath(path))

    # NOTE THAT ARGS IS A TUPLE OF PROPERTY VALUES

    document.storeToURL(
        urlify(arquivo_novo), ())
    document.dispose()
    desktop = smgr.createInstance("com.sun.star.frame.Desktop")    
    desktop.loadComponentFromURL(
        urlify(arquivo_novo), "_blank", 0, ())
    
    os.remove(str(syspath))
    return None


def Delete( ):
    def addAwtModel(oDM,srv,sName,dProps):
        oCM = oDM.createInstance("com.sun.star.awt.UnoControl"+ srv +"Model")
        while dProps:
            prp = dProps.popitem()
            uno.invoke(oCM,"setPropertyValue",(prp[0],prp[1]))
            #works with awt.UnoControlDialogElement only:
            oCM.Name = sName
        oDM.insertByName(sName,oCM)

    '''Salva o arquivo e renomeia'''
    def UserFields(model, nome, valor):
   ### altera o valor do campo nome. 

        master = model.TextFieldMasters.getByName(FIELDMASTER_TEMPLATE % nome)
        master.Content = valor

    # cria uma instancia que permite a insercao no texto

        objfield = model.createInstance("com.sun.star.text.textfield.User")
        objfield.attachTextFieldMaster(master)

        return objfield
        
    context = uno.getComponentContext()
    smgr = context.ServiceManager    
    desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop",context)
    document = desktop.getCurrentComponent()  
    url = document.URL
    try:
        syspath = uno.fileUrlToSystemPath(url)
    except:
        #faz dialogo
        oDM = smgr.createInstance("com.sun.star.awt.UnoControlDialogModel")
        oDM.Title = dialog_label
        addAwtModel(oDM, 'FixedText','lblName',{
            'Label' : error_file_not_saved,
            'Align' : 1,
            }
                    )
                
        addAwtModel(oDM,'Button','btnOK',{
            'Label' : ok_label,
            'DefaultButton' : True,
            'PushButtonType' : 1,
            }
                    )
        
        oDialog = smgr.createInstance("com.sun.star.awt.UnoControlDialog")
        oDialog.setModel(oDM)
        
        h = 25
        y = 20
        for c in oDialog.getControls():
            c.setPosSize(10, y, 300, h, POSSIZE)
            y += h 
        oDialog.setPosSize(400,300,350,y+h,POSSIZE)
        oDialog.setVisible(True)
        x = oDialog.execute()
        if x:
            pass
        else:
            return False
        oDialog.dispose()
        oDM.dispose()
        return None
        
        
        
    texto_arquivo = str(syspath)
    arquivo = texto_arquivo[texto_arquivo.rfind('\\')+1:]
    caminho = texto_arquivo[:texto_arquivo.rfind('\\')+1]
    #faz dialogo
    oDM = smgr.createInstance("com.sun.star.awt.UnoControlDialogModel")
    oDM.Title = dialog_label
    addAwtModel(oDM,'FixedText','lblName',{
        'Label' : delete_label, 
        'Align' : 1,
        }
                )
             
    addAwtModel(oDM,'Button','btnOK',{
        'Label' : ok_label,
        'DefaultButton' : True,
        'PushButtonType' : 1,
        }
                )
    addAwtModel(oDM,'Button','btnCancel',{
        'Label' : cancel_label,
        'PushButtonType' : 2,
        }
                )

    oDialog = smgr.createInstance("com.sun.star.awt.UnoControlDialog")
    oDialog.setModel(oDM)
    txtN = oDialog.getControl('txtName')
    
    h = 25
    y = 20
    for c in oDialog.getControls():
        c.setPosSize(10, y, 400, h, POSSIZE)
        y += h 
    oDialog.setPosSize(300,300,450,y+h,POSSIZE)
    oDialog.setVisible(True)
    x = oDialog.execute()
    if x:
        pass
    else:
        return False
        
    oDialog.dispose()
    oDM.dispose()
    
    def urlify(path):
        return uno.systemPathToFileUrl(os.path.realpath(path))

    # NOTE THAT ARGS IS A TUPLE OF PROPERTY VALUES

    document.dispose()
    
    desktop = smgr.createInstance("com.sun.star.frame.Desktop")
    desktop.loadComponentFromURL( "private:factory/swriter","_blank", 0, () )
    os.remove(str(syspath))
    return None

g_exportedScripts = Rename, Delete,