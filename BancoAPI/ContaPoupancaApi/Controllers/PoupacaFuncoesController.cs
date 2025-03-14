using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using ContaPoupancaApi.Data;
using ContaPoupancaApi.Models;
using Microsoft.EntityFrameworkCore;



// Controllers/ContaPoupancaAcoesController.cs


namespace ContaPoupancaAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PoupancaFuncoesController(ContaPoupancaApiContext context) : ControllerBase
    {
        private readonly ContaPoupancaApiContext _context = context;

        // GET: api/ContaPoupancaAcoes/ConsultarSaldo/5
        [HttpGet("ConsultarSaldo/{id}")]
        public async Task<ActionResult<decimal>> ConsultarSaldo(int id)
        {
            var contaPoupanca = await _context.Poupanca.FindAsync(id);

            if (contaPoupanca == null)
            {
                return NotFound();
            }

            return contaPoupanca.Saldo;
        }

        // POST: api/ContaPoupancaAcoes/Depositar/5
        [HttpPost("Depositar/{id}")]
        public async Task<IActionResult> Depositar(int id, [FromBody] decimal valor)
        {
            var contaPoupanca = await _context.Poupanca.FindAsync(id);

            if (contaPoupanca == null)
            {
                return NotFound();
            }

            contaPoupanca.Saldo += valor;
            await _context.SaveChangesAsync();

            return NoContent();
        }

        // POST: api/ContaPoupancaAcoes/Sacar/5
        [HttpPost("Sacar/{id}")]
        public async Task<IActionResult> Sacar(int id, [FromBody] decimal valor)
        {
            var contaPoupanca = await _context.Poupanca.FindAsync(id);

            if (contaPoupanca == null)
            {
                return NotFound();
            }

            if (contaPoupanca.Saldo < valor)
            {
                return BadRequest("Saldo insuficiente.");
            }

            contaPoupanca.Saldo -= valor;
            await _context.SaveChangesAsync();

            return NoContent();
        }

        // POST: api/ContaPoupancaAcoes/Transferir/5
        [HttpPost("Transferir/{idOrigem}/{idDestino}")]
        public async Task<IActionResult> Transferir(int idOrigem, int idDestino, [FromBody] decimal valor)
        {
            var contaOrigem = await _context.Poupanca.FindAsync(idOrigem);
            var contaDestino = await _context.Poupanca.FindAsync(idDestino);

            if (contaOrigem == null || contaDestino == null)
            {
                return NotFound();
            }

            if (contaOrigem.Saldo < valor)
            {
                return BadRequest("Saldo insuficiente.");
            }

            contaOrigem.Saldo -= valor;
            contaDestino.Saldo += valor;
            await _context.SaveChangesAsync();

            return NoContent();
        }

        // POST: api/ContaPoupancaAcoes/AplicarCorrecao/5
        [HttpPost("AplicarCorrecao/{id}")]
        public async Task<IActionResult> AplicarCorrecao(int id, [FromBody] decimal taxa)
        {
            var contaPoupanca = await _context.Poupanca.FindAsync(id);

            if (contaPoupanca == null)
            {
                return NotFound();
            }

            contaPoupanca.Saldo *= (1 + taxa);
            await _context.SaveChangesAsync();

            return NoContent();
        }
    }
}