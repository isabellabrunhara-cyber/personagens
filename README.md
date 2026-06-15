# 📚 Grafo de Relacionamentos - Estrutura Dinâmica de Personagens

Este repositório contém o mapeamento completo e interativo da rede de conexões entre os personagens do livro, destacando as dinâmicas familiares, alianças estratégicas, rivalidades e os pontos cruciais de intersecção da narrativa (com especial destaque para o papel unificador de **Ross Meyers** e as pontes sociais).

## 📊 Estrutura Visual do Grafo (Renderização Automática)

O grafo abaixo é gerado automaticamente pelo GitHub usando Mermaid. Ele destaca os núcleos em cores e os tipos de conexões na história.

```mermaid
graph TD
    %% Estilos de Cores
    classDef meyers fill:#1f77b4,stroke:#fff,stroke-width:2px,color:#fff;
    classDef boyd fill:#ff7f0e,stroke:#fff,stroke-width:2px,color:#fff;
    classDef lyle fill:#2ca02c,stroke:#fff,stroke-width:2px,color:#fff;
    classDef alex_circle fill:#9467bd,stroke:#fff,stroke-width:2px,color:#fff;
    classDef derek_circle fill:#bcbd22,stroke:#fff,stroke-width:2px,color:#fff;
    classDef central fill:#d62728,stroke:#fff,stroke-width:3px,color:#fff;
    classDef ponte fill:#17becf,stroke:#fff,stroke-width:2px,color:#fff;

    %% Nós Família Meyers
    BillyM[Billy Meyers]:::meyers
    BeatM[Beatrice Meyers]:::meyers
    GaryM[Gary Meyers]:::meyers
    AnneB[Anne Beghin]:::meyers
    RomeoM[Romeo Meyers]:::meyers
    AlexM[Alex Meyers - Protagonista]:::meyers
    SilasM[Silas Meyers]:::meyers
    RossM((Ross Meyers)):::central

    %% Conexões Meyers
    BillyM <--> |Casados| BeatM
    BillyM --> |Pai| GaryM
    BeatM --> |Mãe| GaryM
    GaryM <--> |Casados| AnneB
    GaryM --> |Pai| RomeoM
    GaryM --> |Pai| AlexM
    GaryM --> |Pai| SilasM
    AnneB --> |Mãe| RomeoM
    AnneB --> |Mãe| AlexM
    AnneB --> |Mãe| SilasM

    %% Nós Família Boyd / Smith / Lewis
    CallumB[Callum Boyd]:::boyd
    ArabellaB[Arabella Boyd]:::boyd
    ElsieB[Elsie Boyd]:::boyd
    EileenB[Eileen Boyd]:::boyd
    DavidS[David Smith]:::boyd
    MasonL[Mason Lewis]:::boyd
    DerekB[Derek Boyd - Protagonista]:::boyd
    DianaB[Diana Boyd]:::boyd
    HazelB[Hazel Boyd]:::ponte

    %% Conexões Boyd
    CallumB <--> |Casados| ArabellaB
    CallumB --> |Pai| ElsieB
    CallumB --> |Pai| EileenB
    ArabellaB --> |Mãe| ElsieB
    ArabellaB --> |Mãe| EileenB
    ElsieB <--> |Irmãs Gémeas| EileenB
    ElsieB <--> |Casados| DavidS
    ElsieB --> |Mãe| DerekB
    ElsieB --> |Mãe| DianaB
    DavidS --> |Pai| DerekB
    DavidS --> |Pai| DianaB
    EileenB <--> |Casados| MasonL
    EileenB --> |Mãe| HazelB
    MasonL --> |Pai| HazelB
    
    %% Primos e Pontes
    HazelB -.-> |Primas| DianaB
    HazelB -.-> |Primos| DerekB
    HazelB <==> |Melhores Amigas| AlexM

    %% O Elo Central (Ross e Core Plot)
    RomeoM -.-> |Ex-Relacionamento| DianaB
    RomeoM --> |Pai| RossM
    DianaB --> |Mãe| RossM
    AlexM -.-> |Tia / Convivência Obrigatória| RossM
    AlexM x--x |Rivalidade Intensa| DianaB

    %% Romance Central
    AlexM <==> |Namorados| DerekB

    %% Família Lyle
    FranklinL[Franklin Lyle]:::lyle
    JulieL[Julie Lyle]:::lyle
    GaryM <--> |Melhores Amigos| FranklinL
    FranklinL <--> |Casados| JulieL

    %% Amigos Alex
    CalebW[Caleb Winters]:::alex_circle
    DrewC[Drew Cooper]:::alex_circle
    DanielP[Daniel Park]:::alex_circle
    PhilipL[Philip Lane]:::alex_circle
    HannahL[Hannah Lynch]:::ponte

    AlexM --> |Amigos| CalebW
    AlexM --> |Amigos| DrewC
    AlexM --> |Amigos| PhilipL
    AlexM --> |Círculo Social| DanielP
    DrewC <--> |Namorados| DanielP
    AlexM <--> |Amigos| HannahL

    %% Amigos Derek & Conflitos Cruzados
    BrentH[Brent Harvey]:::derek_circle
    StephenR[Stephen Reid]:::derek_circle
    MeredithR[Meredith Reid]:::derek_circle

    DerekB --> |Amigos| BrentH
    DerekB --> |Amigos| StephenR
    DerekB --> |Amigos| MeredithR
    DerekB <--> |Amigos| HannahL
    StephenR <--> |Irmãos| MeredithR
    
    %% Rivalidades Cruzadas
    CalebW x--x |Rivais| DerekB
    MeredithR x--x |Rivais| AlexM
    MeredithR <--> |Melhores Amigas| DianaB
