import FWCore.ParameterSet.Config as cms

process = cms.Process( "TEST" )
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

#process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.Geometry.GeometryIdeal_cff")
# This is for MC
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
# find the global tag in the DAS under the Configs for given dataset
process.GlobalTag.globaltag = 'MCRUN2_74_V9A::All'
#*********************************** CHOOSE YOUR CHANNEL  *******************************************#
#                                                                                                    #
#CHANNEL         = "VZ_CHANNEL" 
CHANNEL         = "VZnu_CHANNEL" 
VZ_semileptonic = False
VZ_JetMET       = True
#                                                                                                    #
#****************************************************************************************************#

#*********************************** THE SAMPLES ****************************************************#
# choose the sample                                                                     

SAMPLE="RSGravToZZ_kMpl01_50ns_M_1000"
#SAMPLE="BulkGravToZZToZlepZhad_M-600" 
#SAMPLE="BulkGravToZZToZlepZhad_M-800" 
#SAMPLE="BulkGravToZZToZlepZhad_M-1000" 
#SAMPLE="BulkGravToZZToZlepZhad_M-1200" 
#SAMPLE="BulkGravToZZToZlepZhad_M-1400" 
#SAMPLE="BulkGravToZZToZlepZhad_M-1600" 
#SAMPLE="BulkGravToZZToZlepZhad_M-1800" 
#SAMPLE="BulkGravToZZToZlepZhad_M-2000" 
#SAMPLE="BulkGravToZZToZlepZhad_M-2500" 
#SAMPLE="BulkGravToZZToZlepZhad_M-3000" 
#SAMPLE="BulkGravToZZToZlepZhad_M-3500" 
#SAMPLE="BulkGravToZZToZlepZhad_M-4000" 
#SAMPLE="BulkGravToZZToZlepZhad_M-4500" 

### Source
process.load("ExoDiBosonResonances.EDBRCommon.simulation.RunIIDR74X."+SAMPLE)
process.maxEvents.input = -1
#process.maxEvents.input = 1000

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.cerr.FwkReport.limit = 99999999

configXsecs = {  "BulkGravToZZToZlepZhad_M-600"         : 4.0151E-04,
                 "BulkGravToZZToZlepZhad_M-800"         : 7.3592E-05,
                 "BulkGravToZZToZlepZhad_M-1000"        : 1.9648E-05,
                 "BulkGravToZZToZlepZhad_M-1200"        : 6.5205E-06,
                 "BulkGravToZZToZlepZhad_M-1400"        : 2.4833E-06,
                 "BulkGravToZZToZlepZhad_M-1600"        : 8.1645E-07,
                 "BulkGravToZZToZlepZhad_M-1800"        : 3.7583E-07,
                 "BulkGravToZZToZlepZhad_M-2000"        : 2.2636E-07,
                 "BulkGravToZZToZlepZhad_M-2500"        : 4.2349E-08,
                 "BulkGravToZZToZlepZhad_M-3000"        : 9.2671E-09,
                 "BulkGravToZZToZlepZhad_M-3500"        : 4.7064E-09,
                 "BulkGravToZZToZlepZhad_M-4000"        : 1.9530E-09,
                 "BulkGravToZZToZlepZhad_M-4500"        : 8.9900E-10,
                 "RSGravToZZ_kMpl01_50ns_M_1000"        : 1,
              }

configNevents = {"BulkGravToZZToZlepZhad_M-600"         : 50000,
                 "BulkGravToZZToZlepZhad_M-800"         : 50000,
                 "BulkGravToZZToZlepZhad_M-1000"        : 48400,
                 "BulkGravToZZToZlepZhad_M-1200"        : 49200,
                 "BulkGravToZZToZlepZhad_M-1400"        : 50000,
                 "BulkGravToZZToZlepZhad_M-1600"        : 50000,
                 "BulkGravToZZToZlepZhad_M-1800"        : 50000,
                 "BulkGravToZZToZlepZhad_M-2000"        : 50000,
                 "BulkGravToZZToZlepZhad_M-2500"        : 50000,
                 "BulkGravToZZToZlepZhad_M-3000"        : 49200,
                 "BulkGravToZZToZlepZhad_M-3500"        : 50000,
                 "BulkGravToZZToZlepZhad_M-4000"        : 50000,
                 "BulkGravToZZToZlepZhad_M-4500"        : 50000,
                 "RSGravToZZ_kMpl01_50ns_M_1000"        : 29586,
                }

usedXsec = configXsecs[SAMPLE]
usedNevents = configNevents[SAMPLE]

#*******************************************************************************************************#

### Hadronic and leptonic boson.
process.load("ExoDiBosonResonances.EDBRCommon.leptonicZ_cff")
process.load("ExoDiBosonResonances.EDBRCommon.hadronicZ_cff")
process.load("ExoDiBosonResonances.EDBRCommon.hadronicZnu_cff")
#process.load("ExoDiBosonResonances.EDBRCommon.leptonicW_cff")
#process.load("ExoDiBosonResonances.EDBRCommon.hadronicW_cff")

WBOSONCUT = "pt > 200. & sqrt(2.0*daughter(0).pt()*daughter(1).pt()*(1.0-cos(daughter(0).phi()-daughter(1).phi()))) > 50."
ZBOSONCUT = "pt > 200. & 70. < mass < 110."

process.leptonicVFilter = cms.EDFilter(   "CandViewCountFilter",
                                          src = cms.InputTag("leptonicV"),
                                          minNumber = cms.uint32(1),
                                          filter = cms.bool(True) )

process.leptonicVSelector = cms.EDFilter( "CandViewSelector",
                                          src = cms.InputTag("leptonicV"),
                                          cut = cms.string( ZBOSONCUT ), #Change in case of WChannel
                                          filter = cms.bool(True) )

process.bestLeptonicV = cms.EDFilter(    "LargestPtCandSelector",
                                          src = cms.InputTag("leptonicVSelector"),
                                          maxNumber = cms.uint32(1) )

process.hadronicVFilter = cms.EDFilter(   "CandViewCountFilter",
                                          src = cms.InputTag("hadronicV"),
                                          minNumber = cms.uint32(1),
                                          filter = cms.bool(True) )

process.bestHadronicV = cms.EDFilter(    "LargestPtCandSelector",
                                          src = cms.InputTag("hadronicV"),
                                          maxNumber = cms.uint32(1) )

process.graviton = cms.EDProducer(        "CandViewCombiner",
                                          decay = cms.string("bestLeptonicV bestHadronicV"),
                                          checkCharge = cms.bool(False),
                                          cut = cms.string("mass > 400"),
                                          roles = cms.vstring('leptonicV', 'hadronicV') )

process.gravitonFilter =  cms.EDFilter(   "CandViewCountFilter",
                                          src = cms.InputTag("graviton"),
                                          minNumber = cms.uint32(1),
                                          filter = cms.bool(True) )

process.treeDumper = cms.EDAnalyzer(      "EDBRTreeMaker",
                                          isGen           = cms.bool    (  False                     ),
                                          originalNEvents = cms.int32   (  usedNevents               ),
                                          crossSectionPb  = cms.double  (  usedXsec                  ),
                                          targetLumiInvPb = cms.double  (  40.028                    ),
                                          EDBRChannel     = cms.string  (  CHANNEL                   ),
                                          gravitonSrc     = cms.string  ( "graviton"                 ),
                                          metSrc          = cms.string  ( "slimmedMETs"              ),
                                          vertex          = cms.InputTag( "goodOfflinePrimaryVertex" ))

#************************************** SELECT GEN OR RECO ******************************************# 

option = 'RECO' # 'GEN' 

### GEN level studies
if option == 'GEN':
    process.load("ExoDiBosonResonances.EDBRGenStudies.genMuons_cff")
    process.load("ExoDiBosonResonances.EDBRGenStudies.genElectrons_cff")
    process.load("ExoDiBosonResonances.EDBRGenStudies.genFatJets_cff")
    process.load("ExoDiBosonResonances.EDBRGenStudies.genMET_cff")
    process.treeDumper.metSrc = 'genMetTrue'
    process.treeDumper.isGen  = True
    process.hadronicV.cut = cms.string('pt > 200. '
                                       '& (userFloat("ak8GenJetsSoftDropMass") > 50.) '
                                       '& (userFloat("ak8GenJetsSoftDropMass") < 110.)')

### RECO level studies
if option == 'RECO':
    process.load("ExoDiBosonResonances.EDBRCommon.goodJets_cff")
    process.load("ExoDiBosonResonances.EDBRCommon.niceJets_cff")
    process.load("ExoDiBosonResonances.EDBRCommon.goodMET_cff")
    process.load("ExoDiBosonResonances.EDBRCommon.goodVertex_cff")
    process.load("ExoDiBosonResonances.VetoesProducer.photon_Vetoes_cff")
    process.load("ExoDiBosonResonances.VetoesProducer.ele_Vetoes_cff")
    process.hadronicV.cut = cms.string('pt > 200. '
                                       '& (userFloat("ak8PFJetsCHSSoftDropMass") > 50.) '
                                       '& (userFloat("ak8PFJetsCHSSoftDropMass") < 110.)')
    ##-----  FOR NOW NO CUT IN JET MASS  --------------##
    process.hadronicVnu.cut = cms.string('pt > 200. ')
    process.goodMET.cut = "pt > 250"

#***************************************** SEQUENCES **********************************************# 

process.leptonSequence = cms.Sequence(    process.leptonicVSequence +
                                          process.leptonicVFilter   +
                                          process.leptonicVSelector + 
                                          process.bestLeptonicV     )

process.jetSequence = cms.Sequence(       process.fatJetsSequence   +
                                          process.hadronicV         +
                                          process.hadronicVFilter   +
                                          process.bestHadronicV     )

process.gravitonSequence = cms.Sequence(  process.graviton          +
                                          process.gravitonFilter    )

process.analysis = cms.Path(              process.leptonSequence    +
                                          process.jetSequence       +
                                          process.gravitonSequence  +
                                          process.treeDumper        )

if option=='RECO':
   if VZ_semileptonic == True :    
      process.load("ExoDiBosonResonances.EDBRCommon.hltFilter_cff")
      process.load("ExoDiBosonResonances.EDBRLeptons.goodLeptonsProducer_cff")
      from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
      switchOnVIDElectronIdProducer(process, DataFormat.MiniAOD)
      my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.heepElectronID_HEEPV60_cff']
      for idmod in my_id_modules:
          setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)
      process.analysis.replace(process.leptonSequence, 
                               process.hltSequence              +
                               process.egmGsfElectronIDSequence + 
                               process.goodLeptonsProducer      +  
                               process.leptonSequence           ) 

#************************************ TRIGGER REPORT ANALYZER ***************************************#
#                                                                                                    #
# Only supported for VZ channel   
if VZ_semileptonic == True :
   process.load("ExoDiBosonResonances.EDBRGenStudies.selectLeptonicDecay")
   process.load("ExoDiBosonResonances.EDBRGenStudies.selectHadronicDecay")
   process.load("ExoDiBosonResonances.EDBRGenStudies.trigReportAnalyzer_cff")
   process.analysis.replace(process.hltSequence,
                         process.leptonicDecay +
                         process.hadronicDecay +
                         process.hltSequence   )

   process.endpath = cms.EndPath( process.trigReportAnalyzer )
#                                                                                                    #
#****************************************************************************************************#

#***************************************** FILTER MODE **********************************************#
#                                                                                                    #
# True : Events are filtered before the analyzer. TTree is filled with good valudes only             #
# False: Events are filtered inside the analyzed. TTree is filled with dummy values when numCands==0 #
#                                                                                                    #
filterMode = True
### If you're running in signal, you may want to not filter at this level
### but only later at the tree analysis.
if filterMode == False:
    process.hltFilter.triggerConditions = ('*',)
    process.goodLeptons.filter = False
    process.goodElectrons.cut = ""
    process.goodMuons.cut = ""
    process.leptonicVSelector.cut = '70. < mass < 110.'
    process.graviton.cut = ''
#                                                                                                    #
#****************************************************************************************************#

####################################################################################################
###################################  JET-MET CHANNEL  ##############################################
####################################################################################################

if VZ_JetMET == True :
 
    process.hadronicVFilter.src = cms.InputTag("hadronicVnu")
    ## Why the best hadronicV candidate has the largest pt?
    process.bestHadronicV.src   = cms.InputTag("hadronicVnu")

    process.graviton.decay  =  cms.string("goodMET hadronicVnu")
    process.graviton.cut    =  cms.string("")
    process.graviton.roles  =  cms.vstring('goodMET', 'hadronicVnu')


    process.jetSequence.replace(    process.fatJetsSequence, 
                                    process.fatJetsNuSequence  *
                                    process.hadronicVnu        )

    process.jetSequence.remove(process.hadronicV) 

    from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
    switchOnVIDElectronIdProducer(process, DataFormat.MiniAOD)
#    my_el_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_PHYS14_PU20bx25_V2_cff']
#    my_el_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Spring15_50ns_V1_cff']
    my_el_modules = ['RecoEgamma.ElectronIdentification.Identification.heepElectronID_HEEPV60_cff']
    for idmod in my_el_modules:
        setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)

    switchOnVIDPhotonIdProducer(process, DataFormat.MiniAOD)
#    my_pho_modules = ['RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_PHYS14_PU20bx25_V2_cff']
    my_pho_modules = ['RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_Spring15_50ns_V1_cff']
    for idmod in my_pho_modules:
        setupAllVIDIdsInModule(process,idmod,setupVIDPhotonSelection)

    """# Is this a simulation or real data                                                                                                           
    isMC = True
    # Use private JECs since the GTs are not updated                                                                                              
    usePrivateSQlite = True

    #++++++++++++++++++++++ JEC ak4Jets ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ### Setup the private SQLite -- Ripped from PhysicsTools/PatAlgos/test/corMETFromMiniAOD.py                                                    
    ### TO LOAD THE DB FILE
    if usePrivateSQlite:
        from CondCore.DBCommon.CondDBSetup_cfi import *
        import os
        era = "Summer15_50nsV5"
        if isMC :
            era += "_MC"
        else :
            era += "_DATA"
        dBFile = os.path.expandvars(era+".db")
        process.jec = cms.ESSource("PoolDBESSource",
            CondDBSetup,
            connect = cms.string("sqlite_file:"+dBFile),
            toGet =  cms.VPSet(
                cms.PSet(
                    record = cms.string("JetCorrectionsRecord"),
                    tag = cms.string("JetCorrectorParametersCollection_"+era+"_AK4PF"),
                    label= cms.untracked.string("AK4PF")
                ),
                cms.PSet(
                    record = cms.string("JetCorrectionsRecord"),
                    tag = cms.string("JetCorrectorParametersCollection_"+era+"_AK4PFchs"),
                    label= cms.untracked.string("AK4PFchs")
                ),
            )
        )
        process.es_prefer_jec = cms.ESPrefer("PoolDBESSource",'jec')
        ### END (IF)

    ### Apply L2L3 residual corrections -- under development                                                                                        
    applyL2L3Residuals = True

    ### Rerun Jet/MET with updated corrections and recommendations                                                                                  
    if isMC:
        JECLevels = ['L1FastJet', 'L2Relative', 'L3Absolute']
    else :
        if not applyL2L3Residuals :
            JECLevels = ['L1FastJet', 'L2Relative', 'L3Absolute']
        else :
            JECLevels = ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']

    from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD

    runMetCorAndUncFromMiniAOD(process,
        isData = (not isMC),
    )

    runMetCorAndUncFromMiniAOD(process,
        isData = (not isMC),
        pfCandColl = cms.InputTag("noHFCands"),
        postfix = "NoHF"
    )

    if not applyL2L3Residuals :
        process.patPFMetT1T2Corr.jetCorrLabelRes = cms.InputTag("L3Absolute")
        process.patPFMetT1T2SmearCorr.jetCorrLabelRes = cms.InputTag("L3Absolute")
        process.patPFMetT2Corr.jetCorrLabelRes = cms.InputTag("L3Absolute")
        process.patPFMetT2SmearCorr.jetCorrLabelRes = cms.InputTag("L3Absolute")
        process.shiftedPatJetEnDown.jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")
        process.shiftedPatJetEnUp.jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")

        process.patPFMetT1T2CorrNoHF.jetCorrLabelRes = cms.InputTag("L3Absolute")
        process.patPFMetT1T2SmearCorrNoHF.jetCorrLabelRes = cms.InputTag("L3Absolute")
        process.patPFMetT2CorrNoHF.jetCorrLabelRes = cms.InputTag("L3Absolute")
        process.patPFMetT2SmearCorrNoHF.jetCorrLabelRes = cms.InputTag("L3Absolute")
        process.shiftedPatJetEnDownNoHF.jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")
        process.shiftedPatJetEnUpNoHF.jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")

    from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import patJetCorrFactorsUpdated
    process.patJetCorrFactorsReapplyJEC = patJetCorrFactorsUpdated.clone(
        src = cms.InputTag("slimmedJets"),
        levels = JECLevels,
        payload = 'AK4PFchs'
    )

    from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import patJetsUpdated
    process.slimmedJetsRecorrected = patJetsUpdated.clone(
        jetSource = cms.InputTag("slimmedJets"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsReapplyJEC"))
    )

    ### ---------------------------------------------------------------------------
    ### Removing the HF from the MET computation
    ### ---------------------------------------------------------------------------
    useHFCandidates=False #create an additionnal NoHF slimmed MET collection if the option is set to false

    if not useHFCandidates:
        process.noHFCands = cms.EDFilter("CandPtrSelector",
                                     src=cms.InputTag("packedPFCandidates"),
                                     cut=cms.string("abs(pdgId)!=1 && abs(pdgId)!=2 && abs(eta)<3.0")
                                     )


    process.ak4jecSequence  =  cms.Sequence(      process.patJetCorrFactorsReapplyJEC  * 
                                                  process.slimmedJetsRecorrected
                               )        
    """
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#



    process.analysis.replace(       process.jetSequence,
                                    process.VertexSequence           *
                                    process.jetSequence              *
                                    process.metSequence              *  
                                    process.egmGsfElectronIDs        *    
                                    process.elevetoSequence          *
                                    process.egmPhotonIDs             *
                                    process.photonvetoSequence       
#                                    process.ak4jecSequence       
                            )

    process.analysis.remove(process.leptonSequence)
   
###################################################################################################

print "++++++++++ CUTS ++++++++++\n"
print "Graviton cut = "+str(process.graviton.cut)
if VZ_semileptonic == True :
   print "Leptonic V cut = "+str(process.leptonicVSelector.cut) 
   print "Hadronic V cut = "+str(process.hadronicV.cut)
if VZ_JetMET == True :
   print "Hadronic V cut = "+str(process.hadronicVnu.cut)
   print "MET cut = "+str(process.goodMET.cut)
print "\n++++++++++++++++++++++++++"

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("treeEDBR_"+SAMPLE+"sinjec.root")
                                  )


#process.out = cms.OutputModule("PoolOutputModule",
#          fileName = cms.untracked.string('patTuple.root'),
#          outputCommands = cms.untracked.vstring('keep *')
#)
#process.outpath = cms.EndPath(process.out)