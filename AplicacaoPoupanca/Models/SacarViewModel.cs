using System.ComponentModel.DataAnnotations;

namespace AplicacaoPoupanca.Models
{
    public class SacarViewModel
    {
        public int PoupancaId { get; set; }
        [Range(0.01, double.MaxValue, ErrorMessage = " Valor mínimo de R$0.01")]
        public decimal Valor { get; set; }
    }
}
