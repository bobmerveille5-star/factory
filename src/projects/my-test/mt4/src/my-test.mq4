//+------------------------------------------------------------------+
//| my-test.mq4
//+------------------------------------------------------------------+
#property indicator_chart_window
#property indicator_plots 1

extern int Period = 14;
double buffer[];

int init() {
    SetIndexBuffer(0, buffer);
    return 0;
}

int start() {
    int limit = Bars - IndicatorCounted();
    for(int i = limit - 1; i >= 0; i--) buffer[i] = iRSI(NULL, 0, Period, PRICE_CLOSE, i);
    return 0;
}
