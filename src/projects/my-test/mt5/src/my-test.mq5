//+------------------------------------------------------------------+
//| my-test.mq5
//+------------------------------------------------------------------+
#property indicator_chart_window
#property indicator_plots 1

input int Period = 14;

int handle;
double buffer[];

int OnInit() {
    handle = iRSI(NULL, PERIOD_CURRENT, Period, PRICE_CLOSE);
    SetIndexBuffer(0, buffer);
    return INIT_SUCCEEDED;
}

int OnCalculate(int rates, int prev, const double& open[], const double& close[]) {
    double rsi[];
    CopyBuffer(handle, 0, 0, rates, rsi);
    for(int i = 0; i < rates; i++) buffer[i] = rsi[i];
    return rates;
}
