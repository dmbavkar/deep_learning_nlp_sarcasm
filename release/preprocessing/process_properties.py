import sys
import ConfigParser

class PreProcessor:
    def __init__(self,config_file):
	config = ConfigParser.RawConfigParser()
	config.read(config_file)
        try:
	    header = "PropertySection"
	    self.input = config.get(header, "input")
	    self.output = config.get(header, "output")
	    self.both = config.get(header,"both")
	    self.topSim  = config.get(header,"topSim")
            self.separate = config.get(header,"separate")
            self.separate_attention_context = config.get(header, "separate_attention_context")
            self.separate_attention_response = config.get(header, "separate_attention_response")
            self.interaction = config.get(header, "interaction")
            self.lastSent = config.get(header,"lastSent")
	    self.w2v_file = config.get(header,"w2v_file")
            self.w2v_type = config.get(header,"w2v_type")
            self.num_hidden = config.get(header,"num_hidden")
            self.batch_size = config.get(header,"batch_size")
            self.num_epochs = config.get(header,"num_epochs")
            self.lstm = config.get(header,"lstm")
            self.attention = config.get(header,"attention")
            self.attention_words = config.get(header,"attention_words")
        except:
            print("check the parameters that you entered in the config file")
            exit()
