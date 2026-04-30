import hashlib
import numpy as np

class EarthheartKernelSecurity:
    def __init__(self, expected_hash: str, tolerance: float = 1e-5):
        self.expected_hash = expected_hash
        self.tolerance = tolerance

    def verify_integrity(self, file_path: str) -> bool:
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest() == self.expected_hash
        except FileNotFoundError:
            return False

    def detect_anomaly(self, current_output: float, expected_output: float) -> tuple[bool, float]:
        delta = np.abs(current_output - expected_output)
        is_anomalous = delta > self.tolerance
        return is_anomalous, delta

    def optimize_parameters(self, params: np.ndarray, gradient: np.ndarray, learning_rate: float = 0.01) -> np.ndarray:
        optimized_params = params - (learning_rate * gradient)
        return optimized_params


class EarthheartSocialEthics:
    def __init__(self, min_community_dividend_pct: float = 0.60, target_co2_reduction: float = 40000.0):
        self.min_community_dividend_pct = min_community_dividend_pct
        self.target_co2_reduction = target_co2_reduction

    def calculate_social_dividend(self, total_savings: float) -> float:
        return total_savings * self.min_community_dividend_pct

    def assess_environmental_impact(self, current_co2_avoided: float) -> str:
        if current_co2_avoided >= self.target_co2_reduction:
            return "Etica ed Ecosostenibilità: Risultati conformi. Tutela della natura garantita."
        else:
            return "Monitoraggio Etico: Necessario incremento delle prestazioni green."

    def verify_governmental_collaboration(self, government_agreement_active: bool, transparency_index: float) -> str:
        if government_agreement_active and transparency_index >= 0.95:
            return "Conformità istituzionale e trasparenza al 100% raggiunte."
        else:
            return "Attenzione: Verificare la documentazione e i canali di dialogo con le istituzioni."


class EarthheartGreenTransition:
    def __init__(self, total_diesel_savings: float):
        self.total_diesel_savings = total_diesel_savings
        
    def calculate_quantum_allocation(self) -> dict:
        weights = {
            "Turbine da fondo e superficie": 0.30,  # 30%
            "Turbine Sun Flower": 0.25,            # 25%
            "Pavimenti piezoelettrici": 0.20,       # 20%
            "Turbine da tunnel": 0.15,              # 15%
            "Fondo di riserva e R&D": 0.10          # 10%
        }
        allocation = {tech: self.total_diesel_savings * weight for tech, weight in weights.items()}
        return allocation

    def compare_scenarios(self, years: int = 5) -> dict:
        capex = 200000000.0
        total_diesel_cost = 96000000.0 * years
        
        # Risparmio totale (al netto dell'OPEX)
        total_savings = self.total_diesel_savings * years
        
        # Suddivisione del risparmio
        innovator_share = total_savings * 0.20  # Quota per noi
        community_share = total_savings * 0.60
        
        # Utile netto del progetto
        net_balance_earthheart = total_savings - capex
        
        # ROI del Progetto (Utile Netto / CAPEX * 100)
        project_roi = (net_balance_earthheart / capex) * 100
        
        return {
            "Costo totale scenario Diesel": total_diesel_cost,
            "Bilancio netto Earthheart": net_balance_earthheart,
            "ROI del Progetto (%)": project_roi,
            "La Nostra Quota (20%)": innovator_share
        }


if __name__ == "__main__":
    dummy_hash = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    security = EarthheartKernelSecurity(expected_hash=dummy_hash)
    ethics = EarthheartSocialEthics()
    transition = EarthheartGreenTransition(total_diesel_savings=91000000.0)
    
    confronto = transition.compare_scenarios(years=5)
    for scenario, val in confronto.items():
        if "ROI" in scenario:
            print(f"   - {scenario}: {val:.2f}%")
        else:
            print(f"   - {scenario}: ${val:,.2f}")
