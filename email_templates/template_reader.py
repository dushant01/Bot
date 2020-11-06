class TemplateReader:
    def __init__(self):
        pass

    def read_course_template(self,Q_A):
        try:
            if (Q_A =='QA'):
                email_file = open("email_templates/DSM_Template.html", "r")
                email_message = email_file.read()
                return email_message
        except Exception as e:
            print('The exception is ' + str(e))































            """
            if (course_name=='DataScienceMasters'):
                email_file = open("email_templates/DSM_Template.html", "r")
                e
            elif (course_name=='MachineLearningMasters'):
                email_file = open("email_templates/MLM_Template.html", "r")
                email_message = email_file.read()
            elif (course_name == 'DeepLearningMasters'):
                email_file = open("email_templates/DLM_Template.html", "r")
                email_message = email_file.read()
            elif (course_name == 'NLPMasters'):
                email_file = open("email_templates/NLPM_Template.html", "r")
                email_message = email_file.read()
            elif (course_name == 'DataScienceForManagers'):
                email_file = open("email_templates/DSFM_Template.html", "r")
                email_message = email_file.read()
            elif (course_name == 'Vision'):
                email_file = open("email_templates/Vision_Template.html", "r")
                email_message = email_file.read()
            return email_message
        except Exception as e:
            print('The exception is '+str(e))
            """
