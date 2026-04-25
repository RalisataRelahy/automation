using System;
using System.Collections.Generic;

abstract class Vehicule
{
    public string Marque { get; private set; }

    private int vitesse;
    public int Vitesse
    {
        get { return vitesse; }
        set
        {
            if (value >= 0 && value <= 300)
                vitesse = value;
            else
                vitesse = 0;
        }
    }

    public Vehicule(string marque, int vitesse)
    {
        Marque = marque;
        Vitesse = vitesse;
    }

    public virtual void AfficherInfo()
    {
        Console.WriteLine("----- VEHICULE -----");
        Console.WriteLine("Marque : " + Marque);
        Console.WriteLine("Vitesse : " + Vitesse);
    }

    public abstract void Demarrer();

    public void Accelerer(int valeur)
    {
        Vitesse += valeur;
        if (Vitesse > 300) Vitesse = 300;
    }

    public void Freiner(int valeur)
    {
        Vitesse -= valeur;
        if (Vitesse < 0) Vitesse = 0;
    }
}

// Classe Voiture
class Voiture : Vehicule
{
    public int NombrePortes { get; set; }

    public Voiture(string marque, int vitesse, int nbPortes)
        : base(marque, vitesse)
    {
        NombrePortes = nbPortes;
    }

    public override void Demarrer()
    {
        Console.WriteLine("La voiture démarre");
    }

    public override void AfficherInfo()
    {
        base.AfficherInfo();
        Console.WriteLine("Nombre de portes : " + NombrePortes);
    }
}

// Classe Moto
class Moto : Vehicule
{
    public int Cylindree { get; set; }

    public Moto(string marque, int vitesse, int cylindree)
        : base(marque, vitesse)
    {
        Cylindree = cylindree;
    }

    public override void Demarrer()
    {
        Console.WriteLine("La moto démarre");
    }

    public override void AfficherInfo()
    {
        base.AfficherInfo();
        Console.WriteLine("Cylindrée : " + Cylindree);
    }
}

// Programme principal
class Program
{
    static void Main(string[] args)
    {
        List<Vehicule> vehicules = new List<Vehicule>()
        {
            new Voiture("Toyota", 120, 4),
            new Moto("Honda", 90, 600)
        };

        foreach (var v in vehicules)
        {
            v.AfficherInfo();
            v.Demarrer();

            v.Accelerer(50);
            v.Freiner(30);

            Console.WriteLine("Après modification vitesse : " + v.Vitesse);
            Console.WriteLine();
        }
    }
}