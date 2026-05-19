import 'package:flutter/material.dart';

void main() {
  runApp(const LuniarApp());
}

class LuniarApp extends StatelessWidget {
  const LuniarApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Luniar Confeitaria',
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFFff6b9d),
          brightness: Brightness.dark,
        ),
        fontFamily: 'Montserrat',
      ),
      home: const LuniarHomePage(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class LuniarHomePage extends StatefulWidget {
  const LuniarHomePage({Key? key}) : super(key: key);

  @override
  State<LuniarHomePage> createState() => _LuniarHomePageState();
}

class _LuniarHomePageState extends State<LuniarHomePage> {
  final ScrollController _scrollController = ScrollController();
  String selectedFilter = 'todos';
  bool showMobileMenu = false;

  final List<Map<String, String>> produtos = [
    {
      'nome': 'Brownie',
      'descricao': 'Brownie delicioso e cremoso',
      'preco': 'R\$ 8,00',
      'categoria': 'doces-finos',
      'icon': '🍪'
    },
    {
      'nome': 'Torta Cookie de Ninho com Nutela',
      'descricao': 'Torta deliciosa com cookies, ninho crocante e cobertura de nutela',
      'preco': 'R\$ 16,00',
      'categoria': 'tortas',
      'icon': '🍪'
    },
    {
      'nome': 'Torta Cookie',
      'descricao': 'Torta crocante com cookies premium e recheio delicioso',
      'preco': 'R\$ 16,00',
      'categoria': 'tortas',
      'icon': '🍪'
    },
    {
      'nome': 'Torta Cookie de Brigadeiro',
      'descricao': 'Torta deliciosa com cookies crocantes e recheio cremoso de brigadeiro',
      'preco': 'R\$ 16,00',
      'categoria': 'tortas',
      'icon': '🍪'
    },
    {
      'nome': 'Torta Cookie de Doce de Leite',
      'descricao': 'Torta crocante com cookies e doce de leite cremoso',
      'preco': 'R\$ 16,00',
      'categoria': 'tortas',
      'icon': '🍪'
    },
    {
      'nome': 'Palha Italiana',
      'descricao': 'Doce crocante e delicado feito com calda de açúcar caramelizada',
      'preco': 'R\$ 8,00',
      'categoria': 'doces-finos',
      'icon': '🍬'
    },
    {
      'nome': 'Sanduíche Natural',
      'descricao': 'Sanduíche fresco e saudável com ingredientes selecionados',
      'preco': 'R\$ 10,00',
      'categoria': 'salgados',
      'icon': '🥪'
    },
  ];

  final List<Map<String, String>> valores = [
    {'titulo': 'Amor', 'descricao': 'Cada doce é feito com dedicação e carinho', 'icon': '❤️'},
    {'titulo': 'Qualidade', 'descricao': 'Ingredientes selecionados e frescos', 'icon': '🌿'},
    {'titulo': 'Excelência', 'descricao': 'Sabor impecável em cada produção', 'icon': '⭐'},
  ];

  final List<String> galerias = ['🎂', '🕯️', '🧁', '🍬', '🧁', '🍦'];

  List<Map<String, String>> get produtosFiltrados {
    if (selectedFilter == 'todos') {
      return produtos;
    }
    return produtos.where((p) => p['categoria'] == selectedFilter).toList();
  }

  @override
  void dispose() {
    _scrollController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final isMobile = MediaQuery.of(context).size.width < 768;

    return Scaffold(
      backgroundColor: const Color(0xFF000000),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Abrir WhatsApp: (11) 99999-9999')),
          );
        },
        backgroundColor: const Color(0xFF25d366),
        label: const Icon(Icons.whatsapp),
      ),
      body: SingleChildScrollView(
        controller: _scrollController,
        child: Column(
          children: [
            // NAVBAR
            _buildNavbar(isMobile),

            // HERO SECTION
            _buildHero(),

            // SOBRE NÓS
            _buildSobre(isMobile),

            // CARDÁPIO
            _buildCardapio(isMobile),

            // GALERIA
            _buildGaleria(isMobile),

            // ENCOMENDAS
            _buildEncomendas(isMobile),

            // CONTATO
            _buildContato(isMobile),

            // FOOTER
            _buildFooter(),
          ],
        ),
      ),
    );
  }

  Widget _buildNavbar(bool isMobile) {
    return Container(
      color: Colors.white.withOpacity(0.7),
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
      child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              const Text(
                '✨ Luniar',
                style: TextStyle(
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                  color: Color(0xFFff6b9d),
                ),
              ),
              if (!isMobile)
                Row(
                  children: [
                    _buildNavLink('Início'),
                    _buildNavLink('Sobre'),
                    _buildNavLink('Cardápio'),
                    _buildNavLink('Galeria'),
                    _buildNavLink('Encomendas'),
                    _buildNavLink('Contato'),
                  ],
                )
              else
                IconButton(
                  icon: const Icon(Icons.menu),
                  onPressed: () {
                    setState(() => showMobileMenu = !showMobileMenu);
                  },
                ),
            ],
          ),
          if (isMobile && showMobileMenu)
            Column(
              children: [
                _buildNavLink('Início'),
                _buildNavLink('Sobre'),
                _buildNavLink('Cardápio'),
                _buildNavLink('Galeria'),
                _buildNavLink('Encomendas'),
                _buildNavLink('Contato'),
              ],
            ),
        ],
      ),
    );
  }

  Widget _buildNavLink(String text) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
      child: Text(
        text,
        style: const TextStyle(
          color: Color(0xFF1a1a2e),
          fontWeight: FontWeight.w500,
        ),
      ),
    );
  }

  Widget _buildHero() {
    return Container(
      height: 600,
      decoration: const BoxDecoration(
        gradient: LinearGradient(
          colors: [Color(0xFFff6b9d), Color(0xFFc44569)],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
      ),
      child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'Bem-vindo à',
              style: TextStyle(
                fontSize: 18,
                color: Colors.white,
                letterSpacing: 3,
              ),
            ),
            const SizedBox(height: 20),
            const Text(
              'Luniar Confeitaria',
              style: TextStyle(
                fontSize: 48,
                fontWeight: FontWeight.bold,
                color: Colors.white,
              ),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 20),
            const Text(
              'Transformando momentos em doces e memórias',
              style: TextStyle(
                fontSize: 18,
                color: Colors.white70,
                fontStyle: FontStyle.italic,
              ),
            ),
            const SizedBox(height: 40),
            ElevatedButton(
              onPressed: () {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text('Faça seu pedido agora!')),
                );
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.white,
                padding: const EdgeInsets.symmetric(horizontal: 40, vertical: 15),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(50),
                ),
              ),
              child: const Text(
                'Faça seu pedido',
                style: TextStyle(
                  color: Color(0xFFff6b9d),
                  fontWeight: FontWeight.bold,
                  fontSize: 16,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSobre(bool isMobile) {
    return Container(
      color: const Color(0xFF000000),
      padding: const EdgeInsets.symmetric(vertical: 60, horizontal: 20),
      child: Column(
        children: [
          const Text(
            'Sobre Nós',
            style: TextStyle(
              fontSize: 32,
              fontWeight: FontWeight.bold,
              color: Colors.white,
            ),
          ),
          const SizedBox(height: 10),
          Container(
            height: 4,
            width: 80,
            decoration: BoxDecoration(
              gradient: const LinearGradient(
                colors: [Color(0xFFff6b9d), Color(0xFFc44569)],
              ),
              borderRadius: BorderRadius.circular(2),
            ),
          ),
          const SizedBox(height: 40),
          if (isMobile)
            Column(
              children: [
                _buildSobreText(),
                const SizedBox(height: 40),
                _buildSobreImage(),
              ],
            )
          else
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Expanded(child: _buildSobreText()),
                const SizedBox(width: 40),
                Expanded(child: _buildSobreImage()),
              ],
            ),
        ],
      ),
    );
  }

  Widget _buildSobreText() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const Text(
          'Uma História de Amor e Sabor',
          style: TextStyle(
            fontSize: 24,
            fontWeight: FontWeight.bold,
            color: Color(0xFFff6b9d),
          ),
        ),
        const SizedBox(height: 20),
        const Text(
          'Desde o primeiro bolo até hoje, a Luniar Confeitaria é construída sobre um pilar fundamental: muito amor na hora da mão na massa.',
          style: TextStyle(
            fontSize: 14,
            color: Color(0xFFd1d5db),
            height: 1.8,
          ),
        ),
        const SizedBox(height: 15),
        const Text(
          'Cada receita é criada com dedicação, usando apenas os melhores ingredientes selecionados. Nós acreditamos que a confeitação é uma arte que une pessoas e cria memórias doces.',
          style: TextStyle(
            fontSize: 14,
            color: Color(0xFFd1d5db),
            height: 1.8,
          ),
        ),
        const SizedBox(height: 30),
        Column(
          children: valores
              .map((v) => _buildValor(v['titulo']!, v['descricao']!, v['icon']!))
              .toList(),
        ),
      ],
    );
  }

  Widget _buildValor(String titulo, String descricao, String icon) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 20),
      child: Container(
        padding: const EdgeInsets.all(20),
        decoration: BoxDecoration(
          color: const Color(0xFF1a1a1a),
          borderRadius: BorderRadius.circular(15),
          border: Border.all(
            color: const Color(0xFFff6b9d).withOpacity(0.2),
          ),
        ),
        child: Column(
          children: [
            Text(
              icon,
              style: const TextStyle(fontSize: 32),
            ),
            const SizedBox(height: 10),
            Text(
              titulo,
              style: const TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
                color: Colors.white,
              ),
            ),
            const SizedBox(height: 8),
            Text(
              descricao,
              textAlign: TextAlign.center,
              style: const TextStyle(
                fontSize: 13,
                color: Color(0xFFd1d5db),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSobreImage() {
    return Center(
      child: Container(
        width: 250,
        height: 250,
        decoration: BoxDecoration(
          gradient: const LinearGradient(
            colors: [Color(0xFFff6b9d), Color(0xFFc44569)],
          ),
          borderRadius: BorderRadius.circular(15),
        ),
        child: const Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text('🎂', style: TextStyle(fontSize: 80)),
              Text(
                'Foto Artesanal',
                style: TextStyle(color: Colors.white),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildCardapio(bool isMobile) {
    return Container(
      color: const Color(0xFF2a2a2a),
      padding: const EdgeInsets.symmetric(vertical: 60, horizontal: 20),
      child: Column(
        children: [
          const Text(
            'Nosso Cardápio',
            style: TextStyle(
              fontSize: 32,
              fontWeight: FontWeight.bold,
              color: Colors.white,
            ),
          ),
          const SizedBox(height: 30),
          SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            child: Row(
              children: [
                _buildFilterButton('Todos', 'todos'),
                _buildFilterButton('Bolos', 'bolos'),
                _buildFilterButton('Cupcakes', 'cupcakes'),
                _buildFilterButton('Tortas', 'tortas'),
                _buildFilterButton('Doces Finos', 'doces-finos'),
                _buildFilterButton('Salgados', 'salgados'),
              ],
            ),
          ),
          const SizedBox(height: 40),
          GridView.builder(
            shrinkWrap: true,
            physics: const NeverScrollableScrollPhysics(),
            gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: isMobile ? 1 : 3,
              mainAxisSpacing: 20,
              crossAxisSpacing: 20,
              childAspectRatio: 0.8,
            ),
            itemCount: produtosFiltrados.length,
            itemBuilder: (context, index) {
              final produto = produtosFiltrados[index];
              return _buildProdutoCard(produto);
            },
          ),
        ],
      ),
    );
  }

  Widget _buildFilterButton(String label, String value) {
    final isActive = selectedFilter == value;
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 8),
      child: ElevatedButton(
        onPressed: () {
          setState(() => selectedFilter = value);
        },
        style: ElevatedButton.styleFrom(
          backgroundColor: isActive
              ? const Color(0xFFff6b9d)
              : Colors.transparent,
          side: BorderSide(
            color: const Color(0xFFff6b9d),
          ),
          padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 10),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(50),
          ),
        ),
        child: Text(
          label,
          style: TextStyle(
            color: isActive ? Colors.white : const Color(0xFFff6b9d),
            fontWeight: FontWeight.w600,
          ),
        ),
      ),
    );
  }

  Widget _buildProdutoCard(Map<String, String> produto) {
    return Container(
      decoration: BoxDecoration(
        color: const Color(0xFF1a1a1a),
        borderRadius: BorderRadius.circular(15),
        border: Border.all(
          color: const Color(0xFFff6b9d).withOpacity(0.2),
        ),
      ),
      child: Padding(
        padding: const EdgeInsets.all(15),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              height: 120,
              decoration: BoxDecoration(
                gradient: const LinearGradient(
                  colors: [Color(0xFFff6b9d), Color(0xFFc44569)],
                ),
                borderRadius: BorderRadius.circular(12),
              ),
              child: Center(
                child: Text(
                  produto['icon']!,
                  style: const TextStyle(fontSize: 50),
                ),
              ),
            ),
            const SizedBox(height: 15),
            Text(
              produto['nome']!,
              style: const TextStyle(
                fontSize: 14,
                fontWeight: FontWeight.bold,
                color: Colors.white,
              ),
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
            ),
            const SizedBox(height: 8),
            Text(
              produto['descricao']!,
              style: const TextStyle(
                fontSize: 12,
                color: Color(0xFFd1d5db),
              ),
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
            ),
            const SizedBox(height: 12),
            Text(
              produto['preco']!,
              style: const TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
                color: Color(0xFFff6b9d),
              ),
            ),
            const SizedBox(height: 12),
            ElevatedButton(
              onPressed: () {
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(content: Text('Orçamento para ${produto['nome']}')),
                );
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.transparent,
                side: const BorderSide(color: Color(0xFFff6b9d)),
              ),
              child: const Text(
                'Orçamento',
                style: TextStyle(
                  color: Color(0xFFff6b9d),
                  fontSize: 12,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildGaleria(bool isMobile) {
    return Container(
      color: const Color(0xFF000000),
      padding: const EdgeInsets.symmetric(vertical: 60, horizontal: 20),
      child: Column(
        children: [
          const Text(
            'Galeria de Inspirações',
            style: TextStyle(
              fontSize: 32,
              fontWeight: FontWeight.bold,
              color: Colors.white,
            ),
          ),
          const SizedBox(height: 10),
          const Text(
            'Veja alguns de nossos trabalhos anteriores',
            style: TextStyle(
              fontSize: 14,
              color: Color(0xFFd1d5db),
            ),
          ),
          const SizedBox(height: 40),
          GridView.builder(
            shrinkWrap: true,
            physics: const NeverScrollableScrollPhysics(),
            gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: isMobile ? 2 : 3,
              mainAxisSpacing: 15,
              crossAxisSpacing: 15,
              childAspectRatio: 1,
            ),
            itemCount: galerias.length,
            itemBuilder: (context, index) {
              return Container(
                decoration: BoxDecoration(
                  gradient: const LinearGradient(
                    colors: [Color(0xFFff6b9d), Color(0xFFc44569)],
                  ),
                  borderRadius: BorderRadius.circular(15),
                ),
                child: Center(
                  child: Text(
                    galerias[index],
                    style: const TextStyle(fontSize: 60),
                  ),
                ),
              );
            },
          ),
        ],
      ),
    );
  }

  Widget _buildEncomendas(bool isMobile) {
    return Container(
      color: const Color(0xFF000000),
      padding: const EdgeInsets.symmetric(vertical: 60, horizontal: 20),
      child: Column(
        children: [
          const Text(
            'Faça sua Encomenda',
            style: TextStyle(
              fontSize: 32,
              fontWeight: FontWeight.bold,
              color: Colors.white,
            ),
          ),
          const SizedBox(height: 10),
          const Text(
            'Personalize seu doce perfeito',
            style: TextStyle(
              fontSize: 14,
              color: Color(0xFFd1d5db),
            ),
          ),
          const SizedBox(height: 40),
          Container(
            constraints: const BoxConstraints(maxWidth: 600),
            padding: const EdgeInsets.all(25),
            decoration: BoxDecoration(
              color: const Color(0xFF1a1a1a),
              borderRadius: BorderRadius.circular(20),
              border: Border.all(
                color: const Color(0xFFff6b9d).withOpacity(0.2),
              ),
            ),
            child: Column(
              children: [
                _buildFormField('Nome', 'Digite seu nome'),
                const SizedBox(height: 15),
                _buildFormField('Email', 'seu@email.com'),
                const SizedBox(height: 15),
                _buildFormField('Telefone', '(11) 99999-9999'),
                const SizedBox(height: 15),
                _buildFormField('Data', 'DD/MM/YYYY'),
                const SizedBox(height: 15),
                _buildFormField('Tipo de Doce', 'Selecione...'),
                const SizedBox(height: 15),
                TextFormField(
                  decoration: InputDecoration(
                    hintText: 'Observações especiais...',
                    hintStyle: const TextStyle(color: Color(0xFF777777)),
                    filled: true,
                    fillColor: const Color(0xFF2a2a2a),
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(10),
                      borderSide: const BorderSide(color: Color(0xFF333333)),
                    ),
                    enabledBorder: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(10),
                      borderSide: const BorderSide(color: Color(0xFF333333)),
                    ),
                  ),
                  style: const TextStyle(color: Colors.white),
                  maxLines: 5,
                ),
                const SizedBox(height: 25),
                SizedBox(
                  width: double.infinity,
                  child: ElevatedButton(
                    onPressed: () {
                      ScaffoldMessenger.of(context).showSnackBar(
                        const SnackBar(content: Text('Encomenda enviada com sucesso!')),
                      );
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: const Color(0xFFff6b9d),
                      padding: const EdgeInsets.symmetric(vertical: 15),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(50),
                      ),
                    ),
                    child: const Text(
                      'Enviar Encomenda',
                      style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 16,
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildFormField(String label, String hint) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          label,
          style: const TextStyle(
            color: Colors.white,
            fontWeight: FontWeight.w600,
            fontSize: 13,
          ),
        ),
        const SizedBox(height: 8),
        TextFormField(
          decoration: InputDecoration(
            hintText: hint,
            hintStyle: const TextStyle(color: Color(0xFF777777)),
            filled: true,
            fillColor: const Color(0xFF2a2a2a),
            border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10),
              borderSide: const BorderSide(color: Color(0xFF333333)),
            ),
            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10),
              borderSide: const BorderSide(color: Color(0xFF333333)),
            ),
          ),
          style: const TextStyle(color: Colors.white),
        ),
      ],
    );
  }

  Widget _buildContato(bool isMobile) {
    return Container(
      color: const Color(0xFF000000),
      padding: const EdgeInsets.symmetric(vertical: 60, horizontal: 20),
      child: Column(
        children: [
          const Text(
            'Vem falar com a gente',
            style: TextStyle(
              fontSize: 32,
              fontWeight: FontWeight.bold,
              color: Colors.white,
            ),
          ),
          const SizedBox(height: 40),
          if (isMobile)
            Column(
              children: [
                _buildContactInfoGrid(),
                const SizedBox(height: 40),
                _buildMapPlaceholder(),
              ],
            )
          else
            Row(
              children: [
                Expanded(child: _buildContactInfoGrid()),
                const SizedBox(width: 40),
                Expanded(child: _buildMapPlaceholder()),
              ],
            ),
        ],
      ),
    );
  }

  Widget _buildContactInfoGrid() {
    return GridView.builder(
      shrinkWrap: true,
      physics: const NeverScrollableScrollPhysics(),
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2,
        mainAxisSpacing: 20,
        crossAxisSpacing: 20,
        childAspectRatio: 0.9,
      ),
      itemCount: 4,
      itemBuilder: (context, index) {
        final contactos = [
          {'icon': '💬', 'title': 'WhatsApp', 'value': '(11) 99999-9999'},
          {'icon': '📷', 'title': 'Instagram', 'value': '@luniar_confeitaria'},
          {'icon': '📍', 'title': 'Localização', 'value': 'São Paulo - SP'},
          {'icon': '⏰', 'title': 'Horário', 'value': 'Seg-Sex: 10h-19h'},
        ];
        final contact = contactos[index];

        return Container(
          padding: const EdgeInsets.all(15),
          decoration: BoxDecoration(
            color: const Color(0xFF1a1a1a),
            borderRadius: BorderRadius.circular(15),
            border: Border.all(
              color: const Color(0xFFff6b9d).withOpacity(0.2),
            ),
          ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                contact['icon']!,
                style: const TextStyle(fontSize: 32),
              ),
              const SizedBox(height: 10),
              Text(
                contact['title']!,
                style: const TextStyle(
                  fontSize: 14,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
              const SizedBox(height: 8),
              Text(
                contact['value']!,
                textAlign: TextAlign.center,
                style: const TextStyle(
                  fontSize: 12,
                  color: Color(0xFFd1d5db),
                ),
              ),
            ],
          ),
        );
      },
    );
  }

  Widget _buildMapPlaceholder() {
    return Container(
      height: 300,
      decoration: BoxDecoration(
        gradient: const LinearGradient(
          colors: [Color(0xFFff6b9d), Color(0xFFc44569)],
        ),
        borderRadius: BorderRadius.circular(15),
      ),
      child: const Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('🗺️', style: TextStyle(fontSize: 60)),
            SizedBox(height: 15),
            Text(
              'Mapa da Localização',
              style: TextStyle(
                color: Colors.white,
                fontSize: 16,
                fontWeight: FontWeight.bold,
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildFooter() {
    return Container(
      color: const Color(0xFF000000),
      padding: const EdgeInsets.symmetric(vertical: 30, horizontal: 20),
      child: Column(
        children: [
          const Text(
            '© 2024 Luniar Confeitaria. Todos os direitos reservados.',
            textAlign: TextAlign.center,
            style: TextStyle(
              color: Color(0xFF999999),
              fontSize: 12,
            ),
          ),
          const SizedBox(height: 8),
          const Text(
            'Feito com ❤️ para você',
            textAlign: TextAlign.center,
            style: TextStyle(
              color: Color(0xFF999999),
              fontSize: 12,
            ),
          ),
        ],
      ),
    );
  }
}
