using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using AplicacaoPoupanca.Models;
using AplicacaoPoupanca.Data;

namespace AplicacaoPoupanca.Controllers
{
    public class OperacoesController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
