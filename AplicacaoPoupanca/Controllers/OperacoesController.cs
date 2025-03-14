using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using AplicacaoPoupanca.Models;
using AplicacaoPoupanca.Data;
using System.Security.Cryptography.X509Certificates;

namespace AplicacaoPoupanca.Controllers
{
    public class OperacoesController(ApplicationDbContext context) : Controller

    {
       
        private readonly ApplicationDbContext _context = context;

        // GET: Operacoes/consultarSaldo/5
        public async Task<IActionResult> ConsultarSaldo(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var poupanca = await _context.Poupanca.FindAsync(id);
                
            return View(poupanca);
        }
        // GET: Operacoes/Sacar/5
        public IActionResult Sacar(int id)
        {
            return View(new SacarViewModel { PoupancaId = id});
        }
        // POST: Operacoes/Sacar/5
        [HttpPost]
        public async Task<IActionResult> Sacar(SacarViewModel model)
        {
            if (ModelState.IsValid)
            {
                var poupanca = await _context.Poupanca.FindAsync(model.PoupancaId);
                if (poupanca == null)
                {
                    return NotFound();
                }
                if (model.Valor > poupanca.Saldo)
                {
                    ModelState.AddModelError("Valor", "Saldo insuficiente");
                    return View(model);
                }
                poupanca.Saldo -= model.Valor;
                _context.Update(poupanca);
                await _context.SaveChangesAsync();
                return RedirectToAction("ConsultarSaldo", new { id = model.PoupancaId });
            }
            return View(model);
        }
        // GET: Operacoes/Transferencia
        public IActionResult Transferencia()
        {
            return View();
        }
        // POST: Operacoes/Transferir
        public async Task<IActionResult> Transferir(TransferirViewModel model)
        {
            if (ModelState.IsValid)
            {
                var origem = await _context.Poupanca.FindAsync(model.ContaOrigemId);
                var destino = await _context.Poupanca.FindAsync(model.ContaDestinoId);
                if (origem == null || destino == null)
                {
                    return NotFound();
                }
                if (model.Valor > origem.Saldo)
                {
                    ModelState.AddModelError("Valor", "Saldo insuficiente");
                    return View(model);
                }
                origem.Saldo -= model.Valor;
                destino.Saldo += model.Valor;
                _context.Update(origem);
                _context.Update(destino);
                await _context.SaveChangesAsync();
                return RedirectToAction("ConsultarSaldo", new { id = model.ContaOrigemId });
            }
            return View(model);
        }
        // Post: Operacoes/AplicarCorrecao
        [HttpPost]
        public async Task<IActionResult> AplicarCorrecao(CorrecaoViewModel model)
        {
            if (!ModelState.IsValid) 
                return View(model);

            var poupanca = await _context.Poupanca.FindAsync(model.PoupancaId);

            if (poupanca == null)
                return NotFound();
            var taxa = model.Taxa / 100;

            poupanca.Saldo += (1 + taxa);

            await _context.SaveChangesAsync();

            return RedirectToAction(nameof(ConsultarSaldo), new { id = model.PoupancaId });
        }

        
    }
}
