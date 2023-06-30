### **Excel Formula**
根据单元格内的值在不同区间，取不同的值
`IF(AND(C9>=$C$2,C9<=$D$2),$E$2,IF(AND(C9>=$C$3,C9<=$D$3),$E$3,IF(AND(C9>=$C$4,C9<=$D$4),$E$4,IF(AND(C9>=$C$5,C9<=$D$5),$E$5,IF(AND(C9>=$C$6,C9<=$D$6),$E$6,“”))))`