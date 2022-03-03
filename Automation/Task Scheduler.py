import datetime
import win32com.client

scheduler = win32com.client.Dispatch('Schedule.Service')
scheduler.Connect()
root_folder = scheduler.GetFolder('\\')
task_def = scheduler.NewTask(0)

#Create sub folders, or assign values if they already exist
try:
	SecurityFolder = (scheduler.GetFolder('\\Security'))
	
	try:
		ScansFolder = scheduler.GetFolder('\\Security\\Network Scans')
	except:
		ScansFolder = SecurityFolder.CreateFolder("Network Scans")
	
	try:
		AlertFolder = scheduler.GetFolder('\\Security\\Alerts')
	except:
		AlertFolder = SecurityFolder.CreateFolder("Alerts")
		
except:
	SecurityFolder = root_folder.CreateFolder("Security")
	
	try:
		ScansFolder = scheduler.GetFolder('\\Security\\Network Scans')
	except:
		ScansFolder = SecurityFolder.CreateFolder("Network Scans")
	
	try:
		AlertFolder = scheduler.GetFolder('\\Security\\Alerts')
	except:
		AlertFolder = SecurityFolder.CreateFolder("Alerts")

# Create trigger
start_time = datetime.datetime.now() + datetime.timedelta(minutes=5) 	# How often to run tasks
TASK_TRIGGER_TIME = 1 													# How many times to run the task
trigger = task_def.Triggers.Create(TASK_TRIGGER_TIME)					# Creates the Trigger object with the given conditions
trigger.StartBoundary = start_time.isoformat()							# 

# Create action
TASK_ACTION_EXEC = 0
action = task_def.Actions.Create(TASK_ACTION_EXEC)
action.ID = 'DO NOTHING'
action.Path = 'cmd.exe'
action.Arguments = '/c "exit"'

# Set parameters
task_def.RegistrationInfo.Description = 'Test Task'	# Set Description
task_def.Settings.Enabled = True					# Enable Task
task_def.Settings.StopIfGoingOnBatteries = False	# To (not) run the task while only on batteries

# Register task
# If task already exists, it will be updated
TASK_CREATE_OR_UPDATE = 6
TASK_LOGON_NONE = 0
ScansFolder.RegisterTaskDefinition(
    'nmap Scan',  					# Task name
    task_def,						# Imports the task Definition
    TASK_CREATE_OR_UPDATE,
    '',  							# No user
    '',  							# No password
    TASK_LOGON_NONE)