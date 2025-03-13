using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using AplicacaoPoupanca.Models;

namespace AplicacaoPoupanca.Controllers
{
    public class PoupancaController(ApplicationDbContext context) : Controller
    {
        private readonly ApplicationDbContext _context = context;

        // GET: Poupanca
        public async Task<IActionResult> Index()
        {
            return View(await _context.Poupanca.ToListAsync());
        }

        // GET: Poupanca/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var poupanca = await _context.Poupanca
                .FirstOrDefaultAsync(m => m.Id == id);
            if (poupanca == null)
            {
                return NotFound();
            }

            return View(poupanca);
        }

        // GET: Poupanca/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Poupanca/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,NumeroConta,Titular,Saldo,DataCriacao")] Poupanca poupanca)
        {
            if (ModelState.IsValid)
            {
                _context.Add(poupanca);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(poupanca);
        }

        // GET: Poupanca/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var poupanca = await _context.Poupanca.FindAsync(id);
            if (poupanca == null)
            {
                return NotFound();
            }
            return View(poupanca);
        }

        // POST: Poupanca/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,NumeroConta,Titular,Saldo,DataCriacao")] Poupanca poupanca)
        {
            if (id != poupanca.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(poupanca);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!PoupancaExists(poupanca.Id))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction(nameof(Index));
            }
            return View(poupanca);
        }

        // GET: Poupanca/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var poupanca = await _context.Poupanca
                .FirstOrDefaultAsync(m => m.Id == id);
            if (poupanca == null)
            {
                return NotFound();
            }

            return View(poupanca);
        }

        // POST: Poupanca/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var poupanca = await _context.Poupanca.FindAsync(id);
            if (poupanca != null)
            {
                _context.Poupanca.Remove(poupanca);
            }

            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool PoupancaExists(int id)
        {
            return _context.Poupanca.Any(e => e.Id == id);
        }
    }
}
