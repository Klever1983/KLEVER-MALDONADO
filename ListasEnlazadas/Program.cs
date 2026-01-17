using System;

class Nodo
{
    public int Dato;
    public Nodo Siguiente;

    public Nodo(int dato)
    {
        Dato = dato;
        Siguiente = null;
    }
}

class ListaEnlazada
{
    private Nodo cabeza;

    public ListaEnlazada()
    {
        cabeza = null;
    }

    // EJERCICIO 1
    public int ContarElementos()
    {
        int contador = 0;
        Nodo actual = cabeza;

        while (actual != null)
        {
            contador++;
            actual = actual.Siguiente;
        }

        return contador;
    }

    // EJERCICIO 3
    public int BuscarDato(int valor)
    {
        int contador = 0;
        Nodo actual = cabeza;

        while (actual != null)
        {
            if (actual.Dato == valor)
                contador++;

            actual = actual.Siguiente;
        }

        if (contador == 0)
            Console.WriteLine("El dato no fue encontrado.");

        return contador;
    }

    public void InsertarFinal(int dato)
    {
        Nodo nuevo = new Nodo(dato);

        if (cabeza == null)
        {
            cabeza = nuevo;
        }
        else
        {
            Nodo actual = cabeza;
            while (actual.Siguiente != null)
                actual = actual.Siguiente;

            actual.Siguiente = nuevo;
        }
    }
}

class Program
{
    static void Main()
    {
        ListaEnlazada lista = new ListaEnlazada();

        lista.InsertarFinal(4);
        lista.InsertarFinal(7);
        lista.InsertarFinal(4);
        lista.InsertarFinal(9);

        Console.WriteLine("Cantidad de elementos: " + lista.ContarElementos());

        int veces = lista.BuscarDato(4);
        if (veces > 0)
            Console.WriteLine("El dato se encontró " + veces + " veces.");
    }
}
