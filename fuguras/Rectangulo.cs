using System;

// Clase Rectangulo representa un rectángulo geométrico
public class Rectangulo
{
    private double baseRect;
    private double altura;

    public Rectangulo(double baseRect, double altura)
    {
        this.baseRect = baseRect;
        this.altura = altura;
    }

    public double CalcularArea()
    {
        return baseRect * altura;
    }

    public double CalcularPerimetro()
    {
        return 2 * (baseRect + altura);
    }
}
