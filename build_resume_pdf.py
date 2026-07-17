#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o curriculo final (PDF) do Kevin Fernandes Silva - Red Team Junior."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, HRFlowable
)

ACCENT = HexColor("#1F3B57")
GRAY = HexColor("#555555")
BLACK = HexColor("#1A1A1A")

OUT = "/tmp/claude-1000/-tmp-tmp-tVKEwguj8x/b05a02f7-697a-41c0-a65a-899ee4663f98/scratchpad/Kevin_Fernandes_Silva_CV_RedTeam.pdf"

doc = SimpleDocTemplate(
    OUT, pagesize=A4,
    topMargin=0.45 * inch, bottomMargin=0.45 * inch,
    leftMargin=0.65 * inch, rightMargin=0.65 * inch,
    title="Kevin Fernandes Silva - Curriculo Red Team Junior",
    author="Kevin Fernandes Silva",
)

name_style = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=18, textColor=ACCENT, spaceAfter=1, leading=20)
role_style = ParagraphStyle("role", fontName="Helvetica", fontSize=11, textColor=GRAY, spaceAfter=2, leading=13)
contact_style = ParagraphStyle("contact", fontName="Helvetica", fontSize=9.5, textColor=GRAY, spaceAfter=2, leading=12)
section_style = ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=11.5, textColor=ACCENT, spaceBefore=6, spaceAfter=1, leading=13)
sub_style = ParagraphStyle("sub", fontName="Helvetica-Bold", fontSize=10, textColor=ACCENT, spaceBefore=3, spaceAfter=0, leading=12)
sub_plain_style = ParagraphStyle("subplain", fontName="Helvetica-Bold", fontSize=10.5, textColor=ACCENT, spaceBefore=3, spaceAfter=0, leading=12)
italic_style = ParagraphStyle("italic", fontName="Helvetica-Oblique", fontSize=10, textColor=BLACK, spaceBefore=1, spaceAfter=0, leading=12)
body_style = ParagraphStyle("body", fontName="Helvetica", fontSize=10, textColor=BLACK, spaceAfter=2, leading=12.5, alignment=TA_LEFT)
bullet_style = ParagraphStyle("bullet", fontName="Helvetica", fontSize=10, textColor=BLACK, spaceAfter=0, leading=12, leftIndent=0)

story = []

def rule(color=ACCENT, thickness=0.8, space_before=1, space_after=4):
    story.append(Spacer(1, space_before))
    story.append(HRFlowable(width="100%", thickness=thickness, color=color, spaceBefore=0, spaceAfter=space_after))

def section(text):
    story.append(Paragraph(text.upper(), section_style))
    rule(space_before=0, space_after=3)

def sub(text, plain=False):
    story.append(Paragraph(text, sub_plain_style if plain else sub_style))

def italic(text):
    story.append(Paragraph(text, italic_style))

def body(text):
    story.append(Paragraph(text, body_style))

def bullets(items):
    story.append(
        ListFlowable(
            [ListItem(Paragraph(i, bullet_style), bulletColor=ACCENT, value="bulletchar", spaceAfter=1) for i in items],
            bulletType="bullet", start="•", leftIndent=13, bulletFontSize=7.5, spaceBefore=1, spaceAfter=2,
        )
    )

# ---------------------------------------------------------------------------
# CABECALHO
# ---------------------------------------------------------------------------
story.append(Paragraph("Kevin Fernandes Silva", name_style))
story.append(Paragraph("Desenvolvedor Fullstack | Aspirante a Red Team Júnior (Segurança Ofensiva)", role_style))
story.append(Paragraph("São Paulo, Brasil&nbsp;&nbsp;·&nbsp;&nbsp;linkedin.com/in/kevin-fernandes-silva&nbsp;&nbsp;·&nbsp;&nbsp;Inglês avançado", contact_style))
rule(space_before=0, space_after=5)

# ---------------------------------------------------------------------------
# RESUMO
# ---------------------------------------------------------------------------
section("Resumo")
body(
    "Desenvolvedor Fullstack com experiência prática em C#, .NET, Angular, Golang, Python, "
    "Docker e bancos NoSQL (MongoDB, Redis), em transição ativa para Segurança Ofensiva com "
    "foco em Red Team Júnior. Uso recorrente de Nmap para reconhecimento de rede, conhecimento "
    "aplicado de TCP/IP, DNS, VPN e portas, e prática constante na plataforma TryHackMe "
    "complementam uma base técnica que vai além do ferramental: a vivência como desenvolvedor "
    "de sistemas conteinerizados e APIs permite leitura direta de superfícies de ataque reais — "
    "exposição de portas, autenticação, tráfego HTTP/HTTPS. Interesse particular em criptografia, "
    "automação ofensiva em Python e tópicos emergentes de segurança de IA."
)

# ---------------------------------------------------------------------------
# STACK TECNICA
# ---------------------------------------------------------------------------
section("Stack técnica")

sub("Segurança Ofensiva / Redes")
bullets([
    "<b>Nmap</b> — uso prático e recorrente para varredura e reconhecimento de rede",
    "<b>Wireshark</b> — em desenvolvimento ativo; leitura e análise de pacotes",
    "<b>Burp Suite</b> — uso básico (interceptação e manipulação de requisições HTTP)",
    "<b>TCP/IP, DNS, VPN, portas e protocolos de rede</b> — conhecimento aplicado",
    "<b>Linux</b> — uso avançado no dia a dia (administração, SSH, scripting)",
    "<b>SSH</b> — acesso remoto, gestão de chaves e credenciais",
    "<b>Criptografia clássica</b> — César, Vigenère, XOR, análise de frequência",
    "<b>TryHackMe</b> — prática recorrente (reconhecimento, exploração web, fundamentos ofensivos)",
])

sub("Desenvolvimento")
bullets(["C#, .NET, Angular, Golang, Python, Docker, API Gateway, MongoDB, Redis"])

sub("Automação & Dados")
bullets([
    "<b>OCR aplicado (PaddleOCR)</b> — extração e automação de dados",
    "<b>LLMs</b> — conhecimento introdutório e interesse em automação e segurança de IA",
])

# ---------------------------------------------------------------------------
# EXPERIENCIA PROFISSIONAL
# ---------------------------------------------------------------------------
section("Experiência profissional")

sub("HS Prevent — São Paulo, Brasil (1 ano e 5 meses)", plain=True)

italic("Desenvolvedor Fullstack | Tempo integral | set/2025 – atual (11 meses)")
body(
    "Continuidade da atuação como estagiário, assumindo responsabilidade plena sobre manutenção "
    "e desenvolvimento de sistemas em C#, .NET, Angular, Golang e Python, incluindo componentes "
    "conteinerizados em Docker e integração com bancos NoSQL (MongoDB, Redis)."
)

italic("Estagiário de TI | mar/2025 – set/2025 (7 meses)")
bullets([
    "Manutenção e desenvolvimento de sistemas em C#, .NET, Angular, Golang e Python",
    "Manutenção e implementação de conteinerização em Docker",
    "Acesso, análise e modificação de dados em bancos não relacionais (MongoDB, Redis)",
    "Testes funcionais seguindo metodologia definida",
    "Elaboração de documentos de critérios de aceitação para testes e requisitos de implantação, em apoio à equipe de DevOps",
])

# ---------------------------------------------------------------------------
# FORMACAO ACADEMICA
# ---------------------------------------------------------------------------
section("Formação acadêmica")
sub("Universidade Anhanguera São Paulo", plain=True)
body("Análise e Desenvolvimento de Sistemas — fev/2023 – jun/2026 (em andamento)")

# ---------------------------------------------------------------------------
# SEGURANCA DA INFORMACAO - CTFS
# ---------------------------------------------------------------------------
section("Segurança da Informação — Formação prática e CTFs")

sub("TryHackMe — prática recorrente")
body(
    "Uso contínuo da plataforma para reforço prático de reconhecimento de rede, exploração web "
    "e fundamentos de Red Team, em complemento às trilhas estruturadas abaixo."
)

sub("OverTheWire Bandit (níveis 0–12) — Linux, Bash e SSH")
body("Prática progressiva de administração de sistema via terminal, com autenticação remota real via SSH a cada nível.")
bullets([
    "Acesso remoto e autenticação: ssh, login remoto, gestão de credenciais entre níveis",
    "Manipulação de arquivos: nomes com espaços/caracteres especiais, arquivos ocultos (ls -la), identificação de tipo de arquivo (file)",
    "Busca e filtragem: find por tamanho/permissão/dono/grupo, grep para busca textual por padrões",
    "Processamento de dados: sort, uniq, strings (extração de texto de binários)",
    "Encoding e compressão: Base64, ROT13, hexadecimal (xxd), compressão/descompressão encadeada (gzip, bzip2, tar)",
])

sub("OverTheWire Krypton (níveis 0–5) — Criptografia clássica")
bullets([
    "Diferença entre encoding e encriptação",
    "Cifra de César e ROT13 (força bruta e reconhecimento de padrão)",
    "Substituição monoalfabética com análise de frequência",
    "Cifra de Vigenère (criptografia polialfabética)",
    "Criptanálise estatística básica",
])

sub("OverTheWire Natas (níveis 0–6) — Segurança Web")
bullets([
    "Reconhecimento e enumeração web: view-source, robots.txt, descoberta de diretórios/arquivos ocultos",
    "HTTP na prática: inspeção e manipulação de headers (incluindo Referer) com curl, wget e Burp Suite",
    "Sessões e autenticação: análise de cookies, bypass de restrições client-side via DevTools",
    "Code review: leitura de código-fonte PHP, identificação de includes e arquivos de configuração expostos",
])

sub("picoCTF — General Skills")
bullets([
    "Linux/shell: grep, find, pipes, redirecionamento, cron, variáveis de ambiente, permissões",
    "Rede: netcat, requisições web, curl/wget, fundamentos de rede",
    "Dados: Git básico, hashes (md5, sha1, sha256), Base64, hex, ROT13, compressão, regex",
    "Python aplicado a scripts curtos de resolução de desafios",
])

sub("cmd Challenge (níveis 0–20) — Terminal Linux avançado")
bullets([
    "Arquivos e permissões: touch, cp, mv, rm, chmod, chown",
    "Texto e busca: grep, find, head, tail, cut, awk, sed, sort, uniq, wc, tr",
    "Pipes, redirecionamento e processos: |, &lt;, tee, xargs, ps, kill, top",
    "Ambiente: PATH, variáveis de ambiente, wildcards, expansion, escaping, quoting",
])

sub("Imersão Hacker (prof. Robson Costa)")
body("CVE e análise de vulnerabilidades, OSINT, Google Dork, tipos de malware, SEToolkit, Shodan, Wifite, investigação cibernética.")

# ---------------------------------------------------------------------------
# DIFERENCIAIS
# ---------------------------------------------------------------------------
section("Diferenciais")
bullets([
    "Combinação pouco comum entre desenvolvimento fullstack (C#, .NET, Angular, Golang, Python, Docker, API Gateway) e prática ofensiva hands-on (Nmap, Wireshark, TryHackMe, CTFs), permitindo leitura tanto do código quanto do tráfego de rede por trás de uma vulnerabilidade",
    "Interesse particular e aprofundado em criptografia clássica e aplicada",
    "Exposição prática a automação de dados (OCR com PaddleOCR) e a LLMs, incluindo tópicos emergentes de segurança de IA",
    "Perfil analítico e investigativo, validado por prática constante em TryHackMe, OverTheWire e picoCTF",
    "Inglês avançado",
])

doc.build(story)
print("Salvo em:", OUT)
