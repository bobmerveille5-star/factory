//+------------------------------------------------------------------+
//| MyIndicator.mq5                                                   |
//|                                                                  |
//+------------------------------------------------------------------+
#property indicator_chart_window
#property indicator_plots 1
#property indicator_label1  "MyIndicator"
#property indicator_type1   DRAW_LINE
#property indicator_color1  clrBlue
#property indicator_width1   1

input int rsi_period = 14;

int handle;

double buffer[];

int OnInit() {
    SetIndexBuffer(0, buffer);
    PlotIndexSetString(0, PLOT_LABEL, "MyIndicator");
    handle = iRSI(NULL, PERIOD_CURRENT, 14, PRICE_CLOSE);
    if(handle == INVALID_HANDLE) {
        Print("Erreur création handle");
        return INIT_FAILED;
    }
    return INIT_SUCCEEDED;
}

int OnCalculate(const int rates_total,
                const int prev_calculated,
                const datetime &time[],
                const double &open[],
                const double &high[],
                const double &low[],
                const double &close[],
                const long &tick_volume[],
                const long &volume[],
                const int &spread[]) {
    if(rates_total == 0) return 0;
    
    double rsi[];
    CopyBuffer(handle, 0, 0, rates_total, rsi);
    
    int start = (prev_calculated > 0) ? prev_calculated : 0;
    for(int i = start; i < rates_total; i++) {
        buffer[i] = rsi[i];
    }
    
    return rates_total;
}
