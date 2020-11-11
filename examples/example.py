import okex.account_api as account
import okex.futures_api as future
import okex.lever_api as lever
import okex.spot_api as spot
import okex.swap_api as swap
import okex.index_api as index
import okex.option_api as option
import okex.system_api as system
import okex.information_api as information
import json
import datetime


def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"


time = get_timestamp()

if __name__ =='__main__':

    api_key = ""
    secret_key = ""
    passphrase = ""

    # param use_server_time's value is False if is True will use server timestamp
    # param test's value is False if is True will use simulative trading

# account api test
# Fund Account API
    accountAPI = account.AccountAPI(api_key, secret_key, passphrase, False)
    # Fund account information
    # result = accountAPI.get_wallet()
    # Single currency account information
    # result = accountAPI.get_currency('')
    # Fund transfer
    # result = accountAPI.coin_transfer(currency=``, amount='', account_from='', account_to='', type='', sub_account='', instrument_id='', to_instrument_id='')
    # Withdrawal
    # result = accountAPI.coin_withdraw(currency=``, amount='', destination='', to_address=``, trade_pwd='', fee='')
    # Bill flow query
    # result = accountAPI.get_ledger_record(currency=``, after='', before='', limit='', type='')
    # Get recharge address
    # result = accountAPI.get_top_up_address('')
    # Get account asset valuation
    # result = accountAPI.get_asset_valuation(account_type=``, valuation_currency='')
    # Get sub-account balance information
    # result = accountAPI.get_sub_account('')
    # Query the withdrawal records of all currencies
    # result = accountAPI.get_coins_withdraw_record()
    # Query the withdrawal record of a single currency
    # result = accountAPI.get_coin_withdraw_record('')
    # Get all currency recharge records
    # result = accountAPI.get_top_up_records()
    # Get a single currency recharge record
    # result = accountAPI.get_top_up_record(currency=``, after='', before='', limit='')
    # Get currency list
    # result = accountAPI.get_currencies()
    # Withdrawal fee
    # result = accountAPI.get_coin_fee('')

# spot api test
# Coin API
    spotAPI = spot.SpotAPI(api_key, secret_key, passphrase, False)
    # Coin account information
    # result = spotAPI.get_account_info()
    # Single currency account information
    # result = spotAPI.get_coin_account_info('')
    # Bill flow query
    # result = spotAPI.get_ledger_record(currency=``, after='', before='', limit='', type='')
    # Order
    # result = spotAPI.take_order(instrument_id=``, side='', client_oid='', type='', size='', price='', order_type='0', notional='')
    # Batch order
    # result = spotAPI.take_orders([
    # {'instrument_id':'','side':'','type':'','price':'','size':''},
    # {'instrument_id':'','side':'','type':'','price':'','size':''}
    # ])
    # Cancel the specified order
    # result = spotAPI.revoke_order(instrument_id=``, order_id='', client_oid='')
    # Batch cancel orders
    # result = spotAPI.revoke_orders([
    # {'instrument_id':'','order_ids': ['','']},
    # {'instrument_id':'','order_ids': ['','']}
    # ])
    # Get order list
    # result = spotAPI.get_orders_list(instrument_id=``, state='', after='', before='', limit='')
    # Get all unfilled orders
    # result = spotAPI.get_orders_pending(instrument_id=``, after='', before='', limit='')
    # Get order information
    # result = spotAPI.get_order_info(instrument_id=``, order_id='', client_oid='')
    # Get transaction details
    # result = spotAPI.get_fills(instrument_id=``, order_id='', after='', before='', limit='')
    # Order strategy
    # result = spotAPI.take_order_algo(instrument_id=``, mode='', order_type='', size='', side='', trigger_price='', algo_price='', algo_type='')
    # Order strategy cancellation
    # result = spotAPI.cancel_algos(instrument_id=``, algo_ids=['',''], order_type='')
    # Get current account rate
    # result = spotAPI.get_trade_fee()
    # Get order list
    # result = spotAPI.get_order_algos(instrument_id=``, order_type='', status='', algo_id='', before='', after='', limit='')
    # Public-get currency pair information
    # result = spotAPI.get_coin_info()
    # Public-Get in-depth data
    # result = spotAPI.get_depth(instrument_id=``, size='', depth='')
    # Public-Get all ticker information
    # result = spotAPI.get_ticker()
    # Public-get a ticker information
    # result = spotAPI.get_specific_ticker('')
    # Public-Get transaction data
    # result = spotAPI.get_deal(instrument_id=``, limit='')
    # Public-Get K-line data
    # result = spotAPI.get_kline(instrument_id=``, start='', end='', granularity='')
    # Public-Get historical K-line data
    # result = spotAPI.get_history_kline(instrument_id=``, start='', end='', granularity='')

# level api test
# Coin leverage API
    levelAPI = lever.LeverAPI(api_key, secret_key, passphrase, False)
    # Currency margin account information
    # result = levelAPI.get_account_info()
    # Single currency pair account information
    # result = levelAPI.get_specific_account('')
    # Bill flow query
    # result = levelAPI.get_ledger_record(instrument_id=``, after='', before='', limit='', type='')
    # Leverage configuration information
    # result = levelAPI.get_config_info()
    # A certain leverage configuration information
    # result = levelAPI.get_specific_config_info('')
    # Get currency loan record
    # result = levelAPI.get_borrow_coin(status=``, after='', before='', limit='')
    # A currency pair borrowing record
    # result = levelAPI.get_specific_borrow_coin(instrument_id='', status='', after='', before='', limit='')
    # Borrow currency
    # result = levelAPI.borrow_coin(instrument_id=``, currency='', amount='', client_oid='')
    # Refund
    # result = levelAPI.repayment_coin(instrument_id=``, currency='', amount='', borrow_id='', client_oid='')
    # Order
    # result = levelAPI.take_order(instrument_id=``, side='', margin_trading='', client_oid='', type='', order_type='0', price=``, size='', notional= '')
    # Batch order
    # result = levelAPI.take_orders([
    # {'instrument_id':'','side':'','price':'','size':'','margin_trading': '2'},
    # {'instrument_id':'','side':'','price':'','size':'','margin_trading': '2'}
    # ])
    # Cancel the specified order
    # result = levelAPI.revoke_order(instrument_id=``, order_id='', client_oid='')
    # Batch cancel orders
    # result = levelAPI.revoke_orders([
    # {'instrument_id':'','order_ids': ['','']},
    # {'instrument_id':'','client_oids': ['','']}
    # ])
    # Get order list
    # result = levelAPI.get_order_list(instrument_id=``, state='', after='', before='', limit='')
    # Get order information
    # result = levelAPI.get_order_info(instrument_id=``, order_id='', client_oid='')
    # Get all unfilled orders
    # result = levelAPI.get_order_pending(instrument_id=``, after='', before='', limit='')
    # Get transaction details
    # result = levelAPI.get_fills(instrument_id=``, order_id='', after='', before='', limit='')
    # Get leverage
    # result = levelAPI.get_leverage('')
    # Set leverage
    # result = levelAPI.set_leverage(instrument_id='', leverage='')
    # Public-Get marked price
    # result = levelAPI.get_mark_price('')

# future api test
# Delivery contract API
    futureAPI = future.FutureAPI(api_key, secret_key, passphrase, False)
    # All contract holding information
    # result = futureAPI.get_position()
    # Single contract position information
    # result = futureAPI.get_specific_position('')
    # All currency contract account information
    # result = futureAPI.get_accounts()
    # Single currency contract account information
    # result = futureAPI.get_coin_account('')
    # Get contract currency leverage
    # result = futureAPI.get_leverage('')
    # Set contract currency leverage
    # Full warehouse
    # result = futureAPI.set_leverage(underlying=``, leverage='')
    # By warehouse
    # result = futureAPI.set_leverage(underlying=``, leverage='', instrument_id=``, direction='')
    # Bill flow query
    # result = futureAPI.get_ledger(underlying=``, after='', before='', limit='', type='')
    # Order
    # result = futureAPI.take_order(instrument_id=``, type='', price='', size='', client_oid='', order_type='0', match_price='0')
    # Batch order
    # result = futureAPI.take_orders('', [
    # {'client_oid':'','type':'','price':'','size':'','match_price': '0'},
    # {'client_oid':'','type':'','price':'','size':'','match_price': '0'}
    # ])
    # Cancel the specified order
    # result = futureAPI.revoke_order(instrument_id=``, order_id='', client_oid='')
    # Batch cancel orders
    # result = futureAPI.revoke_orders(instrument_id=``, order_ids=['',''])
    # Change Order
    # result = futureAPI.amend_order(instrument_id=``, cancel_on_fail='', order_id='', client_oid='', request_id='', new_size='', new_price='')
    # Batch modify orders
    # result = futureAPI.amend_batch_orders(instrument_id='', amend_data=[
    # {'cancel_on_fail':'','order_id':'','client_oid':'','request_id':'','new_size':'','new_price':''),
    # {'cancel_on_fail':'','order_id':'','client_oid':'','request_id':'','new_size':'','new_price':'')
    # ])
    # Get order list
    # result = futureAPI.get_order_list(instrument_id=``, state='', after='', before='', limit='')
    # Get order information
    # result = futureAPI.get_order_info(instrument_id=``, order_id='', client_oid='')
    # Get transaction details
    # result = futureAPI.get_fills(instrument_id=``, order_id='', after='', before='', limit='')
    # Set contract currency account mode
    # result = futureAPI.set_margin_mode(underlying=``, margin_mode='')
    # Market price is flat
    # result = futureAPI.close_position(instrument_id=``, direction='')
    # Cancel all pending orders for closing
    # result = futureAPI.cancel_all(instrument_id=``, direction='')
    # Get the frozen quantity of contract pending orders
    # result = futureAPI.get_holds_amount('')
    # Order strategy
    # result = futureAPI.take_order_algo(instrument_id=``, type='', order_type=``, size='', trigger_price='', algo_price='', algo_type='')
    # Order strategy cancellation
    # result = futureAPI.cancel_algos(instrument_id=``, algo_ids=[''], order_type='')
    # Get order list
    # result = futureAPI.get_order_algos(instrument_id=``, order_type='', status='', algo_id='', before='', after='', limit='')
    # Get the current fee rate
    # result = futureAPI.get_trade_fee()
    # Increase/decrease margin
    # result = futureAPI.change_margin(instrument_id=``, direction='', type='', amount='')
    # Set up automatic increase of margin by warehouse
    # result = futureAPI.set_auto_margin(underlying=``, type='')
    # Public-Get contract information
    # result = futureAPI.get_products()
    # Public-Get in-depth data
    # result = futureAPI.get_depth(instrument_id=``, size='', depth='')
    # Public-Get all ticker information
    # result = futureAPI.get_ticker()
    # Public-get a ticker information
    # result = futureAPI.get_specific_ticker('')
    # Public-Get transaction data
    # result = futureAPI.get_trades(instrument_id=``, after='', before='', limit='')
    # Public-Get K-line data
    # result = futureAPI.get_kline(instrument_id=``, start='', end='', granularity='')
    # Public-Get index information
    # result = futureAPI.get_index('')
    # Public-get the currency exchange rate
    # result = futureAPI.get_rate()
    # Public-Get estimated delivery price
    # result = futureAPI.get_estimated_price('')
    # Public-get the total platform position
    # result = futureAPI.get_holds('')
    # Public-Get the current limit price
    # result = futureAPI.get_limit('')
    # Public-Get marked price
    # result = futureAPI.get_mark_price('')
    # Public-Get a liquidation order
    # result = futureAPI.get_liquidation(instrument_id=``, status='', limit='', froms='', to='')
    # Public-Get historical settlement/delivery records
    # result = futureAPI.get_history_settlement(instrument_id=``, underlying='', start='', limit='', end='')
    # Public-Get historical K-line data
    # result = futureAPI.get_history_kline(instrument_id=``, start='', end='', granularity='')

# swap api test
# Perpetual Contract API
    swapAPI = swap.SwapAPI(api_key, secret_key, passphrase, False)
    # All contract holding information
    # result = swapAPI.get_position()
    # Single contract position information
    # result = swapAPI.get_specific_position('')
    # All currency contract account information
    # result = swapAPI.get_accounts()
    # Single currency contract account information
    # result = swapAPI.get_coin_account('')
    # Get the user configuration of a contract
    # result = swapAPI.get_settings('')
    # Set the leverage of a contract
    # result = swapAPI.set_leverage(instrument_id='', leverage='', side='')
    # Bill flow query
    # result = swapAPI.get_ledger(instrument_id=``, after='', before='', limit='', type='')
    # Order
    # result = swapAPI.take_order(instrument_id=``, type='', price='', size='', client_oid='', order_type='0', match_price='0')
    # Batch order
    # result = swapAPI.take_orders('', [
    # {'client_oid':'','type':'','price':'','size':''),
    # {'client_oid':'','type':'','price':'','size':''}
    # ])
    # Cancel order
    # result = swapAPI.revoke_order(instrument_id=``, order_id='', client_oid='')
    # Batch Cancellation
    # result = swapAPI.revoke_orders(instrument_id=``, ids=['',''], client_oids=['',''])
    # Change Order
    # result = swapAPI.amend_order(instrument_id=``, cancel_on_fail='', order_id=``, client_oid='', request_id='', new_size='', new_price='')
    # Batch modify orders
    # result = swapAPI.amend_batch_orders(instrument_id='', amend_data=[
    # {'cancel_on_fail':'','order_id':'','client_oid':'','request_id':'','new_size':'','new_price':''),
    # {'cancel_on_fail':'','order_id':'','client_oid':'','request_id':'','new_size':'','new_price':'')
    # ])
    # Get a list of all orders
    # result = swapAPI.get_order_list(instrument_id=``, state='', after='', before='', limit='')
    # Get order information
    # result = swapAPI.get_order_info(instrument_id=``, order_id='', client_oid='')
    # Get transaction details
    # result = swapAPI.get_fills(instrument_id=``, order_id='', after='', before='', limit='')
    # Get the frozen quantity of contract pending orders
    # result = swapAPI.get_holds_amount('')
    # Order strategy
    # result = swapAPI.take_order_algo(instrument_id=``, type='', order_type=``, size='', trigger_price='', algo_price='', algo_type='')
    # Order strategy cancellation
    # result = swapAPI.cancel_algos(instrument_id=``, algo_ids=[''], order_type='')
    # Get order list
    # result = swapAPI.get_order_algos(instrument_id=``, order_type='', status='', algo_id='', before='', after='', limit='')
    # Get account handling fee rate
    # result = swapAPI.get_trade_fee()
    # Market price is flat
    # result = swapAPI.close_position(instrument_id=``, direction='')
    # Cancel all pending orders for closing
    # result = swapAPI.cancel_all(instrument_id=``, direction='')
    # Public-Get contract information
    # result = swapAPI.get_instruments()
    # Public-Get in-depth data
    # result = swapAPI.get_depth(instrument_id=``, size='', depth='')
    # Public-Get all ticker information
    # result = swapAPI.get_ticker()
    # Public-get a ticker information
    # result = swapAPI.get_specific_ticker('')
    # Public-Get transaction data
    # result = swapAPI.get_trades(instrument_id=``, after='', before='', limit='')
    # Public-Get K-line data
    # result = swapAPI.get_kline(instrument_id=``, start='', end='', granularity='')
    # Public-Get index information
    # result = swapAPI.get_index('')
    # Public-get the currency exchange rate
    # result = swapAPI.get_rate()
    # Public-get the total platform position
    # result = swapAPI.get_holds('')
    # Public-Get the current limit price
    # result = swapAPI.get_limit('')
    # Public-Get a liquidation order
    # result = swapAPI.get_liquidation(instrument_id=``, status='', froms='', to='', limit='')
    # Public-Get contract funding rate
    # result = swapAPI.get_funding_time('')
    # Public-Get contract marked price
    # result = swapAPI.get_mark_price('')
    # Public-Get contract historical funding rate
    # result = swapAPI.get_historical_funding_rate(instrument_id=``, limit='')
    # Public-Get historical K-line data
    # result = swapAPI.get_history_kline(instrument_id=``, start='', end='', granularity='')

    # option api test
    # Option contract API
    optionAPI = option.OptionAPI(api_key, secret_key, passphrase, False)
    # Single underlying index position information
    # result = optionAPI.get_specific_position(underlying='', instrument_id='')
    # Single subject account information
    # result = optionAPI.get_underlying_account('')
    # Order
    # result = optionAPI.take_order(instrument_id=``, side='', price='', size='', client_oid='', order_type='0', match_price='0')
    # Batch order
    # result = optionAPI.take_orders('', [
    # {'instrument_id':'','side':'','price':'','size':'','order_type': '0','match_price': '0'},
    # {'instrument_id':'','side':'','price':'','size':'','order_type': '0','match_price': '0'}
    # ])
    # Cancel order
    # result = optionAPI.revoke_order(underlying=``, order_id='', client_oid='')
    # Batch Cancellation
    # result = optionAPI.revoke_orders(underlying='', order_ids=['',''], client_oids=['',''])
    # Change Order
    # result = optionAPI.amend_order(underlying=``, order_id='', client_oid=``, request_id='', new_size='', new_price='')
    # Batch modify orders
    # result = optionAPI.amend_batch_orders('', [
    # {'order_id':'','new_size':''},
    # {'client_oid':'','request_id':'','new_size':''}
    # ])
    # Get the status of a single order
    # result = optionAPI.get_order_info(underlying=``, order_id='', client_oid='')
    # Get order list
    # result = optionAPI.get_order_list(underlying=``, state='', instrument_id=``, after='', before='', limit='')
    # Get transaction details
    # result = optionAPI.get_fills(underlying=``, order_id='', instrument_id=``, after='', before='', limit='')
    # Get bill flow
    # result = optionAPI.get_ledger(underlying=``, after='', before='', limit='')
    # Get the fee rate
    # result = optionAPI.get_trade_fee()
    # Public-Get the underlying index
    # result = optionAPI.get_index()
    # Public-get option contract
    # result = optionAPI.get_instruments(underlying=``, delivery='', instrument_id='')
    # Public-Get detailed pricing of option contracts
    # result = optionAPI.get_instruments_summary(underlying=``, delivery='')
    # Public-Get detailed pricing of a single option contract
    # result = optionAPI.get_option_instruments_summary(underlying=``, instrument_id='')
    # Public-Get in-depth data
    # result = optionAPI.get_depth(instrument_id=``, size='')
    # Public-Get transaction data
    # result = optionAPI.get_trades(instrument_id=``, after='', before='', limit='')
    # Public-get a certain Ticker information
    # result = optionAPI.get_specific_ticker('')
    # Public-Get K-line data
    # result = optionAPI.get_kline(instrument_id=``, start='', end='', granularity='')
    # Public-Get historical settlement/exercise records
    # result = optionAPI.get_history_settlement(instrument_id=``, start='', end='', limit='')

# information api test
# Contract transaction data API
    informationAPI = information.InformationAPI(api_key, secret_key, passphrase, False)
    # Public-ratio of long and short positions
    # result = informationAPI.get_long_short_ratio(currency=``, start='', end='', granularity='')
    # Public-total position and trading volume
    # result = informationAPI.get_volume(currency=``, start='', end='', granularity='')
    # Public-active buying and selling situation
    # result = informationAPI.get_taker(currency=``, start='', end='', granularity='')
    # Public-Long-short elite trend indicator
    # result = informationAPI.get_sentiment(currency=``, start='', end='', granularity='')
    # Public-Long-short elite average holding ratio
    # result = informationAPI.get_margin(currency=``, start='', end='', granularity='')

# index api test
# Index API
    indexAPI = index.IndexAPI(api_key, secret_key, passphrase, False)
    # Public-access index components
    # result = indexAPI.get_index_constituents('')

# system api test
# Get system upgrade status
    system = system.SystemAPI(api_key, secret_key, passphrase, False)
    # Public-Get system upgrade status
    # result = system.get_system_status('')


    print(time + json.dumps(result))
