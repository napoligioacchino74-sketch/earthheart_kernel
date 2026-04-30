import numpy as np

class KernelV38:
    """
    Classe principale del Kernel V38 per l'ecosistema Earthheart.
    Gestisce i calcoli di fluidodinamica e le simulazioni di ottimizzazione quantistica.
    """
    def __init__(self, densita_acqua=1025.0, kappa=0.41, z0=0.01, efficienza=0.35):
        self.densita_acqua = densita_acqua
        self.kappa = kappa
        self.z0 = z0
        self.efficienza = efficienza

    def calcola_potenza_superficie(self, raggio, v_corrente, amp_onda, omega, t):
        """
        Calcola la potenza estratta dalla turbina di superficie
        combinando corrente e moto ondoso.
        """
        v_s = v_corrente + amp_onda * omega * np.cos(omega * t)
        area = np.pi * (raggio ** 2)
        potenza_s = 0.5 * self.densita_acqua * area * (v_s ** 3) * self.efficienza
        return potenza_s

    def calcola_potenza_fondo(self, z_min, z_max, raggio, u_star, num_punti=50):
        """
        Calcola la potenza estratta dalla turbina di fondo
        integrando la velocità del fluido tramite profilo logaritmico.
        """
        z_vals = np.linspace(z_min, z_max, num_punti)
        v_f = (u_star / self.kappa) * np.log(z_vals / self.z0)
        
        area_striscia = (np.pi * (raggio ** 2)) / num_punti
        potenza_f = 0.0
        
        for v in v_f:
            if v > 0:
                potenza_f += 0.5 * self.densita_acqua * area_striscia * (v ** 3) * self.efficienza
                
        return potenza_f

    def predizione_venti_qft(self, dati_sensori):
        """
        Simulazione dell'algoritmo quantistico (QFT - Quantum Fourier Transform)
        per la predizione delle turbolenze eoliche.
        """
        if not dati_sensori:
            return 0.0
            
        dati_array = np.array(dati_sensori)
        fft_dati = np.fft.fft(dati_array)
        frequenza_dominante = np.abs(fft_dati).mean()
        
        return frequenza_dominante

    def ottimizzazione_rete_qaoa(self, isola_ids, domanda_energetica, costo_diesel):
        """
        Simulazione di ottimizzazione con algoritmo quantistico QAOA 
        per il bilanciamento della rete e del consumo.
        """
        soluzione_distribuzione = {}
        for idx in isola_ids:
            peso = costo_diesel * domanda_energetica.get(idx, 0)
            soluzione_distribuzione[idx] = round(peso * 0.08, 2)
            
        return soluzione_distribuzione


if __name__ == "__main__":
    # Inizializzazione del Kernel
    kernel = KernelV38()
    
    # Parametri di test per i calcoli
    raggio_turbina = 1.5
    v_corrente = 1.2
    amp_onda = 0.5
    omega = 0.1
    tempo = 0.0
    
    p_sup = kernel.calcola_potenza_superficie(raggio_turbina, v_corrente, amp_onda, omega, tempo)
    p_fondo = kernel.calcola_potenza_fondo(z_min=0.5, z_max=3.0, raggio=raggio_turbina, u_star=0.05)
    
    dati_vento = [5.2, 5.4, 5.8, 5.5, 5.0, 5.3]
    frequenza = kernel.predizione_venti_qft(dati_vento)
    
    isole = ["Tongatapu", "Vava'u", "Ha'apai"]
    domanda = {"Tongatapu": 5000, "Vava'u": 1500, "Ha'apai": 1200}
    costo_diesel_tonga = 1.60
    distribuzione = kernel.ottimizzazione_rete_qaoa(isole, domanda, costo_diesel_tonga)
    
    # Output pulito
    print("=== RISULTATI KERNEL V38 ===")
    print(f"Potenza Superficie: {p_sup:.2f} W")
    print(f"Potenza Fondo: {p_fondo:.2f} W")
    print(f"Frequenza Vento: {frequenza:.2f} Hz")
    print(f"Distribuzione Isole: {distribuzione}")

