using System.ComponentModel.DataAnnotations;

namespace AplicacaoPoupanca.Models
{
    public class TransferirViewModel
    {
        public int ContaOrigemId { get; set; }
        public int ContaDestinoId { get; set; }
        [Range(0.01, double.MaxValue, ErrorMessage = "Valor mínimo de R$0.01")]
        public decimal Valor { get; set; }
    }
}
