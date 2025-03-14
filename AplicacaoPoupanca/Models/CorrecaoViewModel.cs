using System.ComponentModel.DataAnnotations;

namespace AplicacaoPoupanca.Models
{
    public class CorrecaoViewModel
    {
        public int PoupancaId { get; set; }
        [Range(0.01, 100, ErrorMessage = "Taxa entre 0.01% e 100%")]
        public decimal Taxa { get; set; }
    }
}
