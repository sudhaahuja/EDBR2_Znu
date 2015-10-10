import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/584/00000/C0ED0230-855D-E511-85C6-02163E0170AD.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/587/00000/48131EFA-925D-E511-8E19-02163E0141A9.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/629/00000/56F34851-0D5F-E511-8D43-02163E014642.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/630/00000/B8834DB4-215F-E511-B9B8-02163E0145E6.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/662/00000/AE017509-FA5E-E511-A09F-02163E01423E.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/672/00000/F6A4F737-085F-E511-9EB4-02163E011C56.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/673/00000/8AB05963-F95E-E511-9398-02163E011902.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/674/00000/3C51B3BF-F05E-E511-BBAF-02163E0139A9.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/675/00000/CE1617AE-375F-E511-B76A-02163E013454.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/676/00000/267F9AB7-A35F-E511-84F8-02163E0134D7.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/676/00000/3E4236F5-A35F-E511-8078-02163E0143EB.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/676/00000/4E7780B1-A35F-E511-A67D-02163E0124E6.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/676/00000/E0BF3A62-A45F-E511-96E0-02163E01458F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/676/00000/FE8027B5-A35F-E511-A041-02163E01441A.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/677/00000/7CE0EA21-1E5F-E511-80B6-02163E0079EF.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/721/00000/98E8E8B4-095F-E511-A411-02163E01465C.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/725/00000/AA1B6150-385F-E511-AC63-02163E0134D4.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/727/00000/92B76BA6-3A5F-E511-8EC9-02163E0134FE.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/728/00000/7A52459A-3A5F-E511-972B-02163E0129AD.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/729/00000/4C626602-1560-E511-B447-02163E01445A.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/729/00000/527DDAFE-1460-E511-94E0-02163E014319.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/729/00000/6083CE05-1560-E511-975D-02163E014295.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/729/00000/762BA101-1560-E511-B726-02163E01265F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/729/00000/A4977CE1-1460-E511-9CAA-02163E011EA7.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/734/00000/A8E486B7-BB5F-E511-87E5-02163E0124F4.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/798/00000/A89DAA39-B25F-E511-855E-02163E0145B0.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/801/00000/E64C709C-F65F-E511-BD46-02163E014646.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/834/00000/D84F3CC2-0560-E511-A2DA-02163E014538.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/842/00000/DCDD0A1D-4560-E511-96C2-02163E014294.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/843/00000/780BF79B-F660-E511-B002-02163E01352A.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/843/00000/96A551A7-F660-E511-BCF5-02163E0134C3.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/843/00000/BC746727-F860-E511-98AB-02163E01342E.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/843/00000/F2E32999-F660-E511-947E-02163E014470.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/865/00000/C2E3CEFC-F060-E511-9FBB-02163E012A69.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/866/00000/88057EE2-F660-E511-A5FF-02163E0141D6.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/867/00000/883774CA-1D61-E511-846A-02163E01338B.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/868/00000/3A3600F6-9B61-E511-A98D-02163E0142E7.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/868/00000/56747FF4-9B61-E511-B25A-02163E01457D.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/869/00000/90FFEAC8-1461-E511-9EE3-02163E012798.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/924/00000/940E14B7-6761-E511-8274-02163E013976.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/925/00000/EE892A76-6761-E511-B11D-02163E013738.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/926/00000/AA8680C7-D966-E511-8E4F-02163E01420C.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/935/00000/BCE8270C-9D61-E511-AC4A-02163E014706.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/936/00000/34DCFE75-4562-E511-AADE-02163E01350A.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/936/00000/34E0EA76-4562-E511-843D-02163E01442B.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/936/00000/6000BA79-4562-E511-94D5-02163E011CC4.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/936/00000/682CCD7D-4562-E511-ABC4-02163E011843.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/936/00000/6A2FD27D-4562-E511-98C4-02163E011B9C.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/936/00000/7A29917D-4562-E511-8F1A-02163E013841.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/936/00000/800BD27C-4562-E511-B523-02163E0142E7.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/936/00000/883FCD77-4562-E511-B1CA-02163E014658.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/936/00000/98B606AD-4562-E511-B9BD-02163E011F95.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/936/00000/9E4A8F7B-4562-E511-8DD2-02163E01181F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/936/00000/BCECF77A-4562-E511-A6A0-02163E0134C3.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/936/00000/C8BCAD75-4562-E511-9826-02163E011968.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/936/00000/D27B8778-4562-E511-9F7D-02163E013819.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/941/00000/881EBF88-1362-E511-A26A-02163E014393.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/024/00000/A8467271-2562-E511-93C3-02163E0135AC.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/027/00000/4EF34094-3162-E511-9CAB-02163E01460A.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/394/00000/DA63CDFC-2464-E511-B21E-02163E013700.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/395/00000/C4FC9510-1664-E511-80B3-02163E013470.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/396/00000/34103FF1-8C67-E511-9454-02163E0127CE.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/396/00000/F8E3A4A8-AB6B-E511-96C7-02163E01477C.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/397/00000/82D31E9F-5564-E511-B0EE-02163E011B86.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/398/00000/AA10E174-3F64-E511-90F7-02163E0135C9.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/399/00000/EA17B13B-5C64-E511-AA63-02163E0124DF.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/399/00000/EA480C2D-5C64-E511-BCEB-02163E01364A.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/400/00000/1668155F-6665-E511-92F1-02163E01417E.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/400/00000/2A2DDD07-6865-E511-A035-02163E014616.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/400/00000/A6A8242C-6465-E511-9B78-02163E0145E8.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/400/00000/E6FDA972-6765-E511-9573-02163E014321.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/400/00000/F4816E28-6565-E511-BEED-02163E012036.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/400/00000/FE97EE07-6365-E511-BD7E-02163E0142FF.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/460/00000/2CE43092-DB64-E511-96C1-02163E01275F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/461/00000/5A2591C9-2965-E511-857A-02163E0142E3.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/487/00000/22DE3EFE-9167-E511-907A-02163E0141B6.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/487/00000/32A72952-3F66-E511-8FCC-02163E0123C3.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/487/00000/821F20DB-9167-E511-8B7B-02163E01291F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/487/00000/D28525A9-4066-E511-98A9-02163E0136BF.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/487/00000/E4963CEF-9167-E511-B3C6-02163E01339E.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/487/00000/F863D9EE-9167-E511-9DB7-02163E011A25.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/490/00000/16612AE6-4866-E511-B0FA-02163E011F93.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/490/00000/7671A09F-5767-E511-B2D1-02163E0142EB.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/490/00000/E8491496-5767-E511-A26C-02163E01417C.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/529/00000/5C114375-D365-E511-A01B-02163E01411C.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/531/00000/A61B06F5-2766-E511-B6E4-02163E0133A7.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/598/00000/96B095EC-2A66-E511-8674-02163E01397B.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/599/00000/FA174E8B-5D66-E511-B820-02163E0135A4.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/611/00000/F448BEEE-6366-E511-B8E1-02163E014271.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/613/00000/0AFB8C3F-3A67-E511-9A3D-02163E013625.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/613/00000/1E50231D-3A67-E511-A042-02163E012B92.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/613/00000/4A37AA37-3A67-E511-841C-02163E011C4C.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/613/00000/4EF79C44-3A67-E511-96ED-02163E014621.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/613/00000/5A01CF1F-3A67-E511-A8E1-02163E01263D.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/613/00000/AAF6A328-3A67-E511-A94F-02163E0134C5.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/614/00000/743FC2BE-4067-E511-B2BF-02163E0128F6.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/645/00000/4C7EA9A2-F967-E511-A725-02163E012036.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/645/00000/6000101F-F967-E511-91E1-02163E0134A4.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/645/00000/6AC15E1E-F967-E511-81E4-02163E011F98.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/645/00000/828F4425-F967-E511-ABF1-02163E012502.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/645/00000/9EF24272-6A68-E511-B862-02163E014584.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/682/00000/3E368B07-EB67-E511-B287-02163E011C81.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/721/00000/361199CA-BF67-E511-B650-02163E0144DB.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/722/00000/6415BAD2-E167-E511-8E5B-02163E0143D3.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/723/00000/0EBBD26B-8F68-E511-B66F-02163E01371C.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/732/00000/A0080B8D-D467-E511-BD72-02163E012516.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/735/00000/5E3BAD53-F367-E511-A4D3-02163E011975.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/745/00000/A4D86FE9-3468-E511-9E24-02163E014262.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/748/00000/B4C3D63D-3368-E511-A023-02163E012372.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/751/00000/08C55498-7868-E511-8A06-02163E0126C7.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/751/00000/16C4ADAA-7868-E511-87DD-02163E014346.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/804/00000/22DA4DA7-6968-E511-8ED0-02163E0139B7.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/805/00000/6875294D-8968-E511-B54C-02163E011B48.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/805/00000/F4EFFF3D-8968-E511-AE4E-02163E013740.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/816/00000/002AF78A-AE68-E511-AA29-02163E0144FE.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/816/00000/3CCF5E8D-AE68-E511-8DB5-02163E012273.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/819/00000/6A8356A9-CC68-E511-85A5-02163E011E1D.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/821/00000/1E365AA9-9468-E511-952C-02163E0134A7.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/822/00000/06CF16D1-2969-E511-BB87-02163E011863.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/822/00000/2CF8363E-2A69-E511-ACBE-02163E011B0D.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/822/00000/784141D6-2969-E511-8F4C-02163E013507.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/822/00000/9CBC70D0-2969-E511-BC14-02163E012821.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/822/00000/ECB0AFD9-2969-E511-865E-02163E01478B.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/823/00000/64F8F050-2069-E511-8E56-02163E0142D8.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/824/00000/6AC2E478-0C69-E511-897B-02163E01466F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/825/00000/BC5241A6-0469-E511-8C7F-02163E0145B6.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/933/00000/AEAE161D-4269-E511-A6B8-02163E014120.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/964/00000/185CD731-5A69-E511-9090-02163E01456A.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/968/00000/96A9052D-A669-E511-B8AE-02163E01416B.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/968/00000/FC92E138-A669-E511-8E99-02163E0125CC.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/969/00000/6E09FE7C-CB69-E511-8A7D-02163E011BC3.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/969/00000/A4548B69-CB69-E511-AB1A-02163E011D58.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/257/969/00000/D08175A8-CB69-E511-94D1-02163E013746.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/258/050/00000/C66A6B25-DE69-E511-BAA2-02163E0121CA.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/258/110/00000/DAC10058-286A-E511-B2A1-02163E01429B.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/258/125/00000/589844DD-7D6A-E511-A552-02163E01299C.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/258/129/00000/0414C5D1-EA6A-E511-9E15-02163E01257B.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/258/136/00000/B2DA5A85-AA6A-E511-9880-02163E01462D.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/258/150/00000/96D7F21C-9A6A-E511-AFCF-02163E013710.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/258/152/00000/D8028C79-9B6A-E511-ADE7-02163E0137DC.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/258/155/00000/0809A52A-AA6A-E511-8554-02163E012A6E.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/258/157/00000/EE9EC86A-D96A-E511-B409-02163E011ACB.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/258/158/00000/0A8FC3B0-F46B-E511-A6D0-02163E011E43.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/258/158/00000/3E103BE8-F46B-E511-A69F-02163E011A36.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/258/158/00000/54B062F1-F46B-E511-8AC9-02163E014186.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/258/158/00000/723E1FAC-F46B-E511-93D1-02163E014789.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/258/158/00000/9E284BB0-F46B-E511-9DB4-02163E0125CC.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/258/158/00000/D2E6F9B4-F46B-E511-9881-02163E014787.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/258/158/00000/FCF8DD7A-F56B-E511-9F84-02163E0144B1.root' ] );


secFiles.extend( [
               ] )
