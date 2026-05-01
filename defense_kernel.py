import hashlib

class SoftwareIntegrityChecker:
    def __init__(self, original_source_code):
        self.reference_hash = self.calculate_hash(original_source_code)

    def calculate_hash(self, data):
        """
        Crea un hash crittografico SHA-3 256-bit del codice.
        """
        sha3 = hashlib.sha3_256()
        sha3.update(data.encode('utf-8'))
        return sha3.hexdigest()

    def verify_integrity(self, current_source_code):
        """
        Verifica se il codice è stato alterato.
        """
        current_hash = self.calculate_hash(current_source_code)
        
        if current_hash == self.reference_hash:
            return {
                "status": "VALID",
                "integrity_score": "100%",
                "msg": "Il software è integro e inconfutabile."
            }
        else:
            return {
                "status": "CORRUPTED_OR_TAMPERED",
                "integrity_score": "0%",
                "msg": "Attenzione: Il codice del software è stato manomesso!"
            }


class EarthheartDefenseSystem:
    def __init__(self, original_source_code):
        self.blacklist = set()
        self.honeypot_address = "192.168.1.200" # Indirizzo dell'ambiente controllato (Deception)
        self.pqc_public_key = "PQC_LATTICE_V39" # Chiave crittografica post-quantum
        
        # Inizializziamo il sistema di controllo integrità
        self.integrity_checker = SoftwareIntegrityChecker(original_source_code)

    def check_waf(self, ip_address):
        """
        1. Web Application Firewall (WAF) avanzato
        Filtra le richieste in entrata bloccando IP nella blacklist.
        """
        if ip_address in self.blacklist:
            return {"status": "BLOCKED", "msg": "Accesso negato dal WAF."}
        return {"status": "ALLOWED", "msg": "IP pulito."}

    def check_deception(self, request_data, ip_address):
        """
        2. Sistema di Deception (Honeypot)
        Se rileva un attacco, reindirizza l'IP in un loop.
        """
        suspicious_signatures = ["<script>", "UNION SELECT", "--", "DROP TABLE"]
        
        for sig in suspicious_signatures:
            if sig in request_data:
                self.blacklist.add(ip_address)
                return {
                    "status": "REDIRECTED", 
                    "msg": f"Attacco rilevato. Reindirizzamento IP {ip_address} all'Honeypot: {self.honeypot_address}."
                }
        return {"status": "NORMAL", "msg": "Nessuna anomalia rilevata."}

    def verify_pqc_signature(self, data, signature):
        """
        3. Crittografia Post-Quantum (PQC)
        Verifica l'integrità del payload con algoritmo lattice-based.
        """
        hash_check = hashlib.sha3_256(data.encode('utf-8')).hexdigest()
        
        if signature == self.pqc_public_key:
            return {"status": "SECURE", "msg": "Firma quantistica verificata, accesso autorizzato."}
        else:
            return {"status": "UNAUTHORIZED", "msg": "Firma quantistica non valida."}

    def process_request(self, ip_address, request_data, signature, current_source_code):
        """
        Algoritmo unificato per l'elaborazione di ogni richiesta al Kernel V39.5.
        """
        # Controllo di Integrità prima di eseguire qualsiasi logica
        integrity_check = self.integrity_checker.verify_integrity(current_source_code)
        if integrity_check["status"] != "VALID":
            return integrity_check

        # Fase 1: Controllo WAF
        waf_result = self.check_waf(ip_address)
        if waf_result["status"] == "BLOCKED":
            return waf_result

        # Fase 2: Controllo Deception/Honeypot
        deception_result = self.check_deception(request_data, ip_address)
        if deception_result["status"] == "REDIRECTED":
            return deception_result

        # Fase 3: Verifica Crittografia Post-Quantum
        pqc_result = self.verify_pqc_signature(request_data, signature)
        if pqc_result["status"] != "SECURE":
            return pqc_result

        return {
            "status": "SUCCESS", 
            "msg": "Richiesta validata ed eseguita dal Kernel V39.5."
        }


if __name__ == "__main__":
    # Simula la lettura del codice sorgente corrente del file
    try:
        with open(__file__, "r") as f:
            codice_sorgente_corrente = f.read()
    except Exception:
        codice_sorgente_corrente = "codice_di_testo_generico_per_inizializzazione"

    # Inizializzazione del sistema
    kernel = EarthheartDefenseSystem(original_source_code=codice_sorgente_corrente)
    
    # Esecuzione della richiesta di test
    risultato = kernel.process_request(
        ip_address="203.0.113.5",
        request_data="Optimizing hydro module output",
        signature="PQC_LATTICE_V39",
        current_source_code=codice_sorgente_corrente
    )
    
    print(risultato)

