namespace NinjaTrader.Code.MyIndicator
{
    public class MyIndicator : Indicator
    {
        private double rsiValue;
        
        protected override void Initialize()
        {
            Add(RSI(14, MovingAverageType.Simple));
        }
        
        protected override void OnBarUpdate()
        {
            if(CurrentBar == 0)
            {
                rsiValue = RSI[0];
                Values[0][0] = rsiValue;
                return;
            }
            
            rsiValue = RSI[0];
            Values[0][0] = rsiValue;
        }
    }
}
