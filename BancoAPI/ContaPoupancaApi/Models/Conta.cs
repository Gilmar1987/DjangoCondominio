namespace ContaPoupancaApi.Models
{
    public abstract class Conta
    {
        private int _numeroConta;
        private decimal _saldo;

        public int NumeroConta
        {
            get { return _numeroConta; }
            set
            {
                if (value >= 10000 && value <= 99999)
                {
                    _numeroConta = value;
                }
                else
                {
                    throw new ArgumentException("Número da conta deve ter 5 dígitos.");
                }
            }
        }

        public decimal Saldo
        {
            get { return _saldo; }
            set { _saldo = value; }
        }


    }
}