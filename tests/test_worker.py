from src.cloudtipsadp.clients import WikiClient, SandboxClient, Worker


def test_worker(monkeypatch):
    pass
    # execute_cnt = 0
    # executed_urls = set()
    #
    # def mock_make_get_request(*args, **kwargs):
    #     nonlocal execute_cnt
    #     nonlocal executed_urls
    #     execute_cnt += 1
    #     executed_urls.add(args[0].base_url)
    #
    # monkeypatch.setattr('src.cloudtipsadp.clients.BaseClient'
    #                     '.make_get_request', mock_make_get_request)
    #
    # wiki_url = 'https://test_url_wiki'
    # sandbox_url = 'http://test_url_sandbox'
    #
    # wiki_client = WikiClient(wiki_url)
    # sandbox_client = SandboxClient(sandbox_url)
    #
    # worker = Worker(wiki_client=wiki_client, sandbox_client=sandbox_client)
    # worker()
    # assert execute_cnt == 2
    # assert {wiki_url, sandbox_url} == executed_urls