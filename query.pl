$Testplugs = '+model_data=./data_ddr3+UART_TEST+CPM_CNT_NOFORCE';
print "$Testplugs\n";
if ($Testplugs =~ /\+(\/.*)\//) {
    print "IN"
}