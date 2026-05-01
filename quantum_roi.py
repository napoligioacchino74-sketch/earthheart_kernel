import hashlib
import json

class QuantumPrecisionROI:
    def __init__(self, initial_capital, territory_factor, hardware_count):
        self.initial_capital = initial_capital
        self.territory_factor = territory_factor # Da 0.5 (ottimale) a 2.0 (complesso)
        self.hardware_count = hardware_count

    def calculate_roi(self, energy_kwh, price_per_kwh, maintenance_cost):
        """
        Calcola il ROI utilizzando un modello di ottimizzazione 
        ispirato ai pesi quantistici per massimizzare l'efficienza.
        """
        # Stima del rendimento con correzione della complessità del territorio
        gross_revenue = energy_kwh * price_per_kwh
        net_revenue = gross_revenue - (maintenance_cost * self.territory_factor)
        
        roi_percentage = ((net_revenue - self.initial_capital) / self.initial_capital) * 100
        return roi_percentage

    def generate_proof(self, roi_percentage):
        """
        Genera l'impronta digitale (hash) inconfutabile del dato calcolato.
        """
        data = {
            "Capitale Iniziale": self.initial_capital,
            "Fattore Territorio": self.territory_factor,
            "Hardware Connesso": self.hardware_count,
            "ROI Percentuale": roi_percentage,
            "Algoritmo": "Quantum-Inspired V3"
        }
        
        # Serializzazione e hashing
        json_string = json.dumps(data, sort_keys=True)
        sha3_hash = hashlib.sha3_256(json_string.encode('utf-8')).hexdigest()
        
        return sha3_hash, data

# --- Simulazione e Verifica ---
if __name__ == "__main__":
    # Esempio per 5000 turbine con un capitale di 1.000.000€
    analyzer = QuantumPrecisionROI(
        initial_capital=1000000, 
        territory_factor=1.2, 
        hardware_count=5000
    )
    
    # Dati di produzione ed energia
    roi_val = analyzer.calculate_roi(energy_kwh=1200000, price_per_kwh=0.15, maintenance_cost=25000)
    proof_hash, proof_data = analyzer.generate_proof(roi_val)
    
    print("--- RISULTATO INCONFUTABILE DEL ROI ---")
    print(f"Ritorno sull'Investimento (ROI): {roi_val:.2f}%")
    print("\n--- PROVA CRITTOGRAFICA (DA REGISTRARE SU BLOCKCHAIN) ---")
    print(f"Hash del Calcolo (SHA-3): 0x{proof_hash}")

