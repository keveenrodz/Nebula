# Author: Keveen Rodriguez Zapata <keveenrodriguez@gmail.com>
#
# License: GNU Lesser General Public License v3.0 (LGPLv3)
from PySide2.QtCore import QObject, Slot
from PySide2.QtCore import QSettings
import os


class LoadProject(QObject):
    
    def __init__(self):
        QObject.__init__(self)
        self.name_project = ""
        self.project_to_load = ""
        self.path = ""
        self.settings = QSettings("Nebula")
        self.signal_path = []
        self.signal_value_path = []
    
    @Slot(str, result = 'QString')
    def create(self, name_project):
        """
        
        :param name_project: Name of the project
        :return: path of the settings file
        """
        self.name_project = name_project
        #print("from python " + self.name_project)
        self.settings = QSettings("Nebula", self.name_project)
        self.settings.beginGroup("Project")
        self.settings.setValue("Path", os.path.join(os.environ['HOME'], '.config/Nebula', self.name_project + '.conf'))
        self.settings.setValue("Name", self.name_project)
        self.settings.endGroup()
        self.settings.beginGroup("SignalFiles")
        self.settings.setValue("Path", "None")  # Paths of the signals
        self.settings.endGroup()
        print(self.settings.fileName())
        
        return self.settings.fileName()
    
    @Slot(str, result='QString')
    def settings_dir(self, past_path):
        return self.settings.fileName()

    @Slot(str)
    def load(self, project):
        self.project_to_load = project
        print(f'Project path loaded: {self.project_to_load}')
        head_tail = os.path.split(self.project_to_load)
        self.name_project = head_tail[1].replace(".conf", "")
        del head_tail
        print(f'Project Name loaded: {self.name_project}')
        self.settings = QSettings("Nebula", self.name_project)
        self.settings.beginGroup("Project")
        self.path = self.settings.value("Path")
        self.name_project = self.settings.value("Name")
        self.settings.endGroup()
        self.settings.beginGroup("SignalFiles")
        self.signal_path = self.settings.value("Path")
        self.signal_value_path = self.settings.value("ValuePath")
        self.settings.endGroup()
        print(f'Organization name: {self.settings.organizationName(), self.settings.fileName()}')
        print(f'Loading signal files: {self.signal_path}') # Necesito eviarlo a que cargue la señal
        

        
        
        
        
        
        
        
        
    