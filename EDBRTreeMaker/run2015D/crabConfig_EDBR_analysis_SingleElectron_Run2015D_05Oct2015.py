from CRABClient.UserUtilities import config
config = config()
config.General.transferOutputs = True
config.General.transferLogs = True

config.General.requestName = 'EDBR_SingleElectron_2015D_25ns_05Oct2015'

config.General.workArea = 'EDBR_crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'analysis-SingleElectron_Run2015D_25ns_17-Nov_05Oct2015.py'



config.section_('Data')
config.Data.inputDataset= '/SingleElectron/Run2015D-05Oct2015-v1/MINIAOD'
config.Data.unitsPerJob = 200
config.Data.splitting = 'LumiBased'
config.Data.lumiMask = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt"
config.Data.publication = False
config.Data.useParent = False


config.Data.publication = False
## User options
config.section_("User")
#config.User.email = 'dromeroa@cern.ch'
## Site options
config.section_("Site")
config.Site.storageSite = 'T2_BR_SPRACE'
