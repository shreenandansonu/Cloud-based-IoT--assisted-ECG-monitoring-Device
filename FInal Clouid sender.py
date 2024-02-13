import gspread as gc
import time
import serial
import serial.tools.list_ports


# Get a list of available serial ports
available_ports = list(serial.tools.list_ports.comports())

# Print information about each available port
for port in available_ports:
    gc=gc.service_account(filename='apikey.json')
    sheet=gc.open_by_key('1B5UxbJQ9euV5pNHbRVOFW1cLMwpBMbyf2WzxwmH5AWY')
    worksheet1=sheet.worksheet(title='AUGUST')
    worksheet2=sheet.worksheet(title='RECORD')
    worksheet2.clear()

    ard_data=serial.Serial('COM6',9600)
    time.sleep(1)
    #data_array=np.zeros(20)
    t=1
    t1=time.time
    while True:
        while(ard_data.inWaiting()==0):
            pass
        k=1
        data=ard_data.readline()
        data=str(data,'utf-8')
        data=data.strip('\r\n')
        data_array=data
        while(k<200):
            data=ard_data.readline()
            data=str(data,'utf-8')
            data=data.strip('\r\n')
            print(data)
            data_array=data_array+" "+data
            k=k+1
        data_array=data_array+" "
        worksheet2.update_cell(t,1,data_array)

        t=t+1