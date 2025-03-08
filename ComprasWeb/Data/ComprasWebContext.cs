using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using ComprasWeb.Models;

    public class ComprasWebContext : DbContext
    {
        public ComprasWebContext (DbContextOptions<ComprasWebContext> options)
            : base(options)
        {
        }

        public DbSet<ComprasWeb.Models.Produto> Produto { get; set; } = default!;
    }
