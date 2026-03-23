//+------------------------------------------------------------------+
//| MyIndicator.mq4                                                    |
//|                                                                  |
//+------------------------------------------------------------------+
#property indicator_chart_window
#property indicator_plots 1
#property indicator_label1  "MyIndicator"
#property indicator_type1   DRAW_LINE
#property indicator_color1  clrBlue
#property indicator_width1   1

#property indicator_separate_window

extern int rsi_period = 14;

int handle;
double buffer[];

int init() {
    SetIndexBuffer(0, buffer);
    handle = iRSI(NULL, 0, 14, PRICE_CLOSE);
    if(handle < 0) {
        Print("Erreur création handle");
        return INIT_FAILED;
    }
    return 0;
}

int start() {
    int counted = IndicatorCounted();
    if(counted < 0) return -1;
    
    int limit = Bars - counted;
    for(int i = 0; i < limit; i++) {
        buffer[i] = iRSI(NULL, 0, 14, PRICE_CLOSE, i);
    }
    
    return 0;
}
