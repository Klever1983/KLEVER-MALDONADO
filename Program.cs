using System;
using System.Collections.Generic;
using System.Linq;

namespace VacunacionCovid
{
    class Program
    {
        static void Main(string[] args)
        {
            // Conjunto de 500 ciudadanos
            HashSet<string> ciudadanos = GenerarCiudadanos(500);

            // 75 vacunados con Pfizer
            HashSet<string> pfizer = GenerarVacunados(ciudadanos, 75, 1);

            // 75 vacunados con AstraZeneca
            HashSet<string> astraZeneca = GenerarVacunados(ciudadanos, 75, 50);

            // Unión (vacunados con al menos una dosis)
            HashSet<string> vacunados = new HashSet<string>(pfizer);
            vacunados.UnionWith(astraZeneca);

            // Ciudadanos no vacunados
            HashSet<string> noVacunados = new HashSet<string>(ciudadanos);
            noVacunados.ExceptWith(vacunados);

            // Ciudadanos con ambas dosis (intersección)
            HashSet<string> ambasDosis = new HashSet<string>(pfizer);
            ambasDosis.IntersectWith(astraZeneca);

            // Solo Pfizer
            HashSet<string> soloPfizer = new HashSet<string>(pfizer);
            soloPfizer.ExceptWith(astraZeneca);

            // Solo AstraZeneca
            HashSet<string> soloAstra = new HashSet<string>(astraZeneca);
            soloAstra.ExceptWith(pfizer);

            // Mostrar resultados
            MostrarLista("Ciudadanos NO vacunados", noVacunados);
            MostrarLista("Ciudadanos con ambas dosis", ambasDosis);
            MostrarLista("Ciudadanos SOLO Pfizer", soloPfizer);
            MostrarLista("Ciudadanos SOLO AstraZeneca", soloAstra);
        }

        static HashSet<string> GenerarCiudadanos(int cantidad)
        {
            HashSet<string> lista = new HashSet<string>();

            for (int i = 1; i <= cantidad; i++)
            {
                lista.Add($"Ciudadano {i}");
            }

            return lista;
        }

        static HashSet<string> GenerarVacunados(HashSet<string> ciudadanos, int cantidad, int inicio)
        {
            HashSet<string> vacunados = new HashSet<string>();

            int contador = 0;

            foreach (var ciudadano in ciudadanos.Skip(inicio))
            {
                vacunados.Add(ciudadano);
                contador++;

                if (contador == cantidad)
                    break;
            }

            return vacunados;
        }

        static void MostrarLista(string titulo, HashSet<string> lista)
        {
            Console.WriteLine($"\n===== {titulo} ({lista.Count}) =====");

            foreach (var item in lista)
            {
                Console.WriteLine(item);
            }
        }
    }
}
