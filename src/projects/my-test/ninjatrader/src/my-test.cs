namespace MyIndicator {
    public class my-test : Indicator {
        protected override void Initialize() { Add(RSI(14)); }
        protected override void OnBarUpdate() { Values[0][0] = RSI[0]; }
    }
}
