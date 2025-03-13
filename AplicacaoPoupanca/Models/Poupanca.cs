using System.ComponentModel.DataAnnotations;

namespace AplicacaoPoupanca.Models
{
    public class Poupanca
    {
        [Key]
        public int Id { get; set; }

        [Required(ErrorMessage = "Número da Conta é obrigatório")]
        public string? NumeroConta { get; set; }

        [Required(ErrorMessage = "Titular obrigatório")]
        public string? Titular { get; set; }

        [DataType(DataType.Currency)]
        public decimal Saldo { get; set; }

        public DateTime DataCriacao { get; set; }
    }
}
