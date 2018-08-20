echo "Job: $1"
cd $CMSSW_BASE/src/genproductions/test/calculateXSectionAndFilterEfficiency
cmsenv

ls -lrth

DATASET=`sed -n "$((${1}+1))p" < datasets.txt`
echo DATASET

echo $DATASET > datasets_$((${1}+1)).txt


./calculateXSectionAndFilterEfficiency.sh -f datasets_$((${1}+1)).txt -c Fall17MiniAODv2 -d MINIAODSIM -n 1000000
cd -
cp $CMSSW_BASE/src/genproductions/test/calculateXSectionAndFilterEfficiency/*.log ${SE_INPUT_PATH/dir:\/\/}
