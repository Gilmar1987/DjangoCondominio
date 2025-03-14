using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ContaPoupancaApi.Models;
using ContaPoupancaApi.Data;

namespace ContaPoupancaApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PoupancaController(ContaPoupancaApiContext context) : ControllerBase
    {
        private readonly ContaPoupancaApiContext _context = context;

        // GET: api/Poupanca
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Poupanca>>> GetPoupanca()
        {
            return await _context.Poupanca.ToListAsync();
        }

        // GET: api/Poupanca/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Poupanca>> GetPoupanca(int id)
        {
            var poupanca = await _context.Poupanca.FindAsync(id);

            if (poupanca == null)
            {
                return NotFound();
            }

            return poupanca;
        }

        // PUT: api/Poupanca/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutPoupanca(int id, Poupanca poupanca)
        {
            if (id != poupanca.Id)
            {
                return BadRequest();
            }

            _context.Entry(poupanca).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!PoupancaExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }

        // POST: api/Poupanca
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Poupanca>> PostPoupanca(Poupanca poupanca)
        {
            _context.Poupanca.Add(poupanca);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetPoupanca", new { id = poupanca.Id }, poupanca);
        }

        // DELETE: api/Poupanca/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeletePoupanca(int id)
        {
            var poupanca = await _context.Poupanca.FindAsync(id);
            if (poupanca == null)
            {
                return NotFound();
            }

            _context.Poupanca.Remove(poupanca);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool PoupancaExists(int id)
        {
            return _context.Poupanca.Any(e => e.Id == id);
        }
    }
}
