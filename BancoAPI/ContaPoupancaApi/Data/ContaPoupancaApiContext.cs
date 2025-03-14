using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using ContaPoupancaApi.Models;

namespace ContaPoupancaApi.Data
{
    public class ContaPoupancaApiContext(DbContextOptions<ContaPoupancaApiContext> options) : DbContext(options)
    {
        public DbSet<Poupanca> Poupanca { get; set; } = default!;
    }
}