class ErroBanco(Exception):
    """Classe base para todos os erros do sistema bancário."""
    pass


class ValorInvalidoError(ErroBanco):
    """Erro quando o valor informado é inválido ou não numérico."""
    pass


class SaldoInsuficienteError(ErroBanco):
    """Erro quando o saldo + limite não são suficientes para a operação."""
    pass


class TipoInvalidoError(ErroBanco):
    """Erro quando um objeto de tipo errado é enviado ao banco."""
    pass

class ContaNaoEncontradaError(ErroBanco):
    """Erro quando a conta informada não existe."""
    pass


class AgenciaNaoEncontradaError(ErroBanco):
    """Erro quando a agência informada não está cadastrada."""
    pass


class ClienteNaoEncontradoError(ErroBanco):
    """Erro quando um cliente não é encontrado no sistema."""
    pass


class SenhaIncorretaError(ErroBanco):
    """Erro quando a senha digitada não corresponde com a da conta."""
    pass


class AcessoNegadoError(ErroBanco):
    """Erro quando o cliente não tem permissão para uma operação."""
    pass


class LimiteExcedidoError(ErroBanco):
    """Erro quando o valor ultrapassa o limite permitido pela conta."""
    pass


class OperacaoNaoPermitidaError(ErroBanco):
    """Erro para operações não disponíveis nesse tipo de conta."""
    pass


class ContaJaExistenteError(ErroBanco):
    """Erro quando tenta criar uma conta com número já existente."""
    pass


class AgenciaJaExistenteError(ErroBanco):
    """Erro quando tenta criar uma agência já cadastrada."""
    pass


class ClienteJaExistenteError(ErroBanco):
    """Erro quando tenta cadastrar um cliente já existente."""
    pass


class FormatoInvalidoError(ErroBanco):
    """Erro quando um campo possui formato incorreto (CPF, CNPJ, telefone etc.)."""
    pass


class ValorNegativoError(ErroBanco):
    """Erro para valores menores que zero."""
    pass


class OperacaoCanceladaError(ErroBanco):
    """Erro quando uma operação é cancelada pelo usuário."""
    pass


class LimiteDeTransacoesErro(ErroBanco):
    """Erro quando o cliente ultrapassa o limite diário de transações."""
    pass


class DataInvalidaError(ErroBanco):
    """Erro quando uma data é inválida ou impossível."""
    pass
