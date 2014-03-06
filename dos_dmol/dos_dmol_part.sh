#!/bin/bash

##DMol3 density-of-states calculator by Daniel Yoo 17 November 2013
##Original version and concepts are provided by Michael Lee and Johnny Kim in MTG
##Input file: outmol  (from dmol calculation)
##Output file: DOS_$path.dat, TDOS_$path.dat, TDOS_$path.ipf, Ef_$path
##TDOS_$path contains the information of only total density of states of the system.
##DOS_$path contains all information including total and partial dos.
##TDOS_$path.ipf is the style file for igor plotting.
##Ef_$path contains the Fermi energy in eV unit.

##elapsed time set1
START=$(date +%s)

##Find the current folder name
export current=$(pwd)
path=$(basename $current)
echo $path

##Find fermi energy and prep DOS source
Ef=$(cat outmol |grep Fermi |awk '{printf"%10.4f",$5}')
EfeV=$(echo "scale=8; $Ef*27.211396132" |bc)
Efigor=$(printf "%0.2f" $EfeV)
echo E_$path   TD_$path >>./TDOS_$path.dat
echo -n E_$path   TD_$path " " >>./DOS_$path.dat
grep -A502 DOS outmol >TDOS
grep Atom outmol >atom_list
Natom=$(grep -c Atom outmol)
echo "$path" "Fermi level (eV)" "$EfeV" >>./Ef_$path
echo "Fermi energy, Ef=" "$EfeV" "eV" 
echo "Set Ef to zero"

##Make PDOS_title
echo "Pick atoms to collect"
for a in `seq 1 1 $Natom`
do
Atomnum=$(sed -n ''$a'p' < atom_list |awk '{printf $2}')
Atomname=$(sed -n ''$a'p' < atom_list |awk '{printf $3}')
echo $Atomnum $Atomname
  if [ $Atomnum -ge 10 ]
  then
     grep -A502 "Atom   $Atomnum" outmol >dosp_"$Atomname"_"$Atomnum"
  else
     grep -A502 "Atom    "$Atomnum"" outmol >dosp_"$Atomname"_"$Atomnum"
  fi
echo -n PD_"$path"_"$Atomname"_"$Atomnum"_"s" PD_"$path"_"$Atomname"_"$Atomnum"_"p" PD_"$path"_"$Atomname"_"$Atomnum"_"d" " " >>./DOS_$path.dat
done
echo  >>./DOS_$path.dat

##make combined_DOS data for igor
echo "combined_total_and_partial_dos_in_progress"
for c in `seq -w 2 1 502`
do
E=$(sed -n ''$c'p' < TDOS |awk '{printf"%10.5f",$1}')
EeV=$(echo "scale=6; $E*27.211396132" |bc)
dos=$(sed -n ''$c'p' < TDOS | awk '{printf"%10.5f",$2}')
aE=$(echo "scale=8 ; $EeV- $EfeV"  |bc)
echo "$aE" "$dos" >>./TDOS_$path.dat
echo -n "$aE" "$dos" >>./DOS_$path.dat
for b in `seq 1 1 $Natom`
do
Atomnum=$(sed -n ''$b'p' < atom_list |awk '{printf $2}')
Atomname=$(sed -n ''$b'p' < atom_list |awk '{printf $3}')
doss=$(sed -n ''$c'p' < ./dosp_"$Atomname"_"$Atomnum" |awk '{printf"%10.5f",$1}')
dosp=$(sed -n ''$c'p' < ./dosp_"$Atomname"_"$Atomnum" |awk '{printf"%10.5f",$2}')
dosd=$(sed -n ''$c'p' < ./dosp_"$Atomname"_"$Atomnum" |awk '{printf"%10.5f",$3}')  
echo -n "$doss" "$dosp" "$dosd" >>./DOS_$path.dat
done
echo  >>./DOS_$path.dat
d=$(echo "scale=6; ($c- 2)/ 501* 100" |bc)
echo -ne ""$d"%\r"
done
echo " "
rm TDOS* dosp* atom*


##make igor style file
#cat > ./TDOS_$path.ipf << qwer
#pragma rtGlobals=1
#Window ig_$path() : Graph
#        PauseUpdate; Silent 1           // building window...
#        Display /W=(451,398,1025,822) TD_$path vs E_$path
#        ModifyGraph width=453.543,height=340.157
#        ModifyGraph lSize=1.5
#        ModifyGraph rgb=(0,0,0)
#        ModifyGraph tick=2
#        ModifyGraph zero(bottom)=9
#        ModifyGraph mirror=1
#        ModifyGraph font="Times New Roman"
#        ModifyGraph fSize=20
#        ModifyGraph lblMargin(left)=9
#        ModifyGraph standoff=0
#        ModifyGraph lblLatPos(left)=-4
#        ModifyGraph manTick(left)={0,200,0,0},manMinor(left)={1,50}
#        Label left "\\Z20Density-of-states (arb.)"
#        Label bottom "\\Z20Energy, E-E\\BF\\M\\Z20 (eV)"
#        SetAxis bottom -6,6
#        TextBox/C/N=text1/F=0/A=MC/X=-19.82/Y=41.18 "\\F'Times New Roman'\\Z18TD_$path"
#        Legend/C/N=text0/J/F=0/B=1/A=MC/X=30.18/Y=34.41 "\\F'Times New Roman'\\Z20\r\\s(TD_$path) TDOS\rE\\BF\\M\\Z20 = $Efigor eV"
#EndMacro
#qwer

##elapsed time set2
END=$(date +%s)
DIFF=$(echo "$END- $START" | bc)
echo "Elapsed time" "$DIFF" "sec"

